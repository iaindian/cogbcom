#!/usr/bin/env python3
import argparse
import json
import logging
import os
import time
from pathlib import Path
from urllib.parse import urlencode

import requests

def load_prompts(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['positive'], data['negative']

def find_input_images(input_dir):
    p = Path(input_dir)
    imgs = sorted(x.name for x in p.iterdir()
                  if x.is_file() and x.suffix.lower() in ('.png','.jpg','.jpeg','.bmp','.webp'))
    if not imgs:
        raise FileNotFoundError(f"No images in {input_dir}")
    return imgs

def upload_images(images, input_dir, host):
    """
    POST each image file to /upload/image so the server stores it under ComfyUI/input.
    According to the ComfyUI API, fields are:
      - image: (filename, fileobj, mime)
      - type: "input"
      - overwrite: "true"
    :contentReference[oaicite:2]{index=2}
    """
    url = f"{host.rstrip('/')}/upload/image"
    for name in images:
        fp = Path(input_dir) / name
        with open(fp, 'rb') as f:
            files = {
                'image': (name, f, 'application/octet-stream')
            }
            data = {
                'type': 'input',
                'overwrite': 'true'
            }
            resp = requests.post(url, files=files, data=data)
        try:
            resp.raise_for_status()
            logging.info(f"Uploaded {name}")
        except Exception as e:
            logging.error(f"Failed to upload {name}: {resp.status_code} {resp.text}")
            raise

def load_workflow(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def inject_prompts_and_images(workflow, pos, neg, images):
    pos_done = neg_done = False
    img_idx = 0
    for node_id, node in workflow.items():
        cls = node.get('class_type','')
        inputs = node.setdefault('inputs', {})
        if cls == 'CLIPTextEncode':
            if not pos_done:
                inputs['text'] = pos
                pos_done = True
            elif not neg_done:
                inputs['text'] = neg
                neg_done = True
        elif cls == 'LoadImage' and img_idx < len(images):
            inputs['path'] = images[img_idx]
            # inputs['image'] = images[img_idx]
            logging.debug(f"→ {node_id}: path ← {images[img_idx]}")
            img_idx += 1
    return workflow

def strip_reactor_nodes(workflow):
    removed = [nid for nid,n in workflow.items()
               if n.get('class_type','').startswith('ReActor')]
    for nid in removed:
        del workflow[nid]
    logging.info(f"Removed reactor nodes: {removed}")
    return workflow

# def queue_workflow(workflow, host):
#     url = f"{host.rstrip('/')}/prompt"
#     resp = requests.post(url, json={'prompt': workflow, })
#     if resp.status_code != 200:
#         logging.error(f"POST /prompt → {resp.status_code} {resp.text}")
#         resp.raise_for_status()
#     pid = resp.json().get('prompt_id') or resp.json().get('id')
#     if not pid:
#         raise RuntimeError(f"No prompt_id returned: {resp.text}")
#     logging.info(f"Queued, prompt_id={pid}")
#     return pid


def queue_workflow(workflow, host):
    url = f"{host.rstrip('/')}/prompt"
    # tell ComfyUI exactly which node IDs to collect as outputs
    payload = {
        'prompt': workflow,
        'outputs': ['203', '204'],   # your SaveImage node IDs
    }
    resp = requests.post(url, json=payload)
    if resp.status_code != 200:
        logging.error(f"POST /prompt → {resp.status_code} {resp.text}")
        resp.raise_for_status()
    pid = resp.json().get('prompt_id') or resp.json().get('id')
    if not pid:
        raise RuntimeError(f"No prompt_id returned: {resp.text}")
    logging.info(f"Queued, prompt_id={pid}")
    return pid


def await_completion(prompt_id, host, interval, timeout):
    url = f"{host.rstrip('/')}/history/{prompt_id}"
    deadline = time.time() + timeout
    while time.time() < deadline:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            if 'output' in data:
                logging.info("Done.")
                return data['output']
        else:
            logging.warning(f"GET /history/{prompt_id} → {r.status_code}")
        time.sleep(interval)
    raise TimeoutError(f"Prompt {prompt_id} timed out")

def download_outputs(outputs, host, out_dir):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    for entry in outputs:
        params = {
            'filename': entry['filename'],
            'subfolder': entry.get('subfolder',''),
            'type': entry.get('type','output'),
        }
        url = f"{host.rstrip('/')}/view?{urlencode(params)}"
        r = requests.get(url)
        if r.status_code != 200:
            logging.error(f"GET /view → {r.status_code} {r.text}")
            r.raise_for_status()
        fn = Path(out_dir)/entry['filename']
        fn.write_bytes(r.content)
        logging.info(f"Saved {fn}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--api-json", required=True)
    p.add_argument("--prompt-file", required=True)
    p.add_argument("--input-dir", default="input")
    p.add_argument("--output-dir", default="compyui/output")
    p.add_argument("--host", default="http://127.0.0.1:8188")
    p.add_argument("--bypass-reactor", action="store_true")
    p.add_argument("--poll-interval", type=float, default=1.0)
    p.add_argument("--timeout", type=float, default=300.0)
    p.add_argument("--log-level", default="INFO")
    args = p.parse_args()

    logging.basicConfig(level=getattr(logging, args.log_level.upper()),
                        format="%(asctime)s %(levelname)s %(message)s")

    pos, neg = load_prompts(args.prompt_file)
    imgs = find_input_images(args.input_dir)
    upload_images(imgs, args.input_dir, args.host)

    workflow = load_workflow(args.api_json)
    workflow = inject_prompts_and_images(workflow, pos, neg, imgs)

    if args.bypass_reactor:
        workflow = strip_reactor_nodes(workflow)

    pid = queue_workflow(workflow, args.host)
    outputs = await_completion(pid, args.host,
                                args.poll_interval, args.timeout)
    download_outputs(outputs, args.host, args.output_dir)

if __name__ == "__main__":
    main()
