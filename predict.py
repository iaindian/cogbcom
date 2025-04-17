import os
import subprocess
import threading
import time
import uuid
import json
import urllib.request
import urllib.parse
import websocket
from PIL import Image
from io import BytesIO
from pathlib import Path as SysPath
from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self):
        self.server_address = "127.0.0.1:8188"
        self.start_server()

    def start_server(self):
        server_thread = threading.Thread(target=self.run_server)
        server_thread.daemon = True
        server_thread.start()
        while not self.is_server_running():
            print("⏳ Waiting for ComfyUI server to start...")
            time.sleep(2)
        print("✅ ComfyUI server is up!")

    def run_server(self):
        command = "python ComfyUI/main.py --listen --port 8188"
        subprocess.Popen(command, shell=True, cwd=os.getcwd())

    def is_server_running(self):
        try:
            with urllib.request.urlopen(f"http://{self.server_address}/history/123") as response:
                return response.status == 200
        except:
            return False

    def queue_prompt(self, prompt, client_id):
        data = json.dumps({"prompt": prompt, "client_id": client_id}).encode("utf-8")
        req = urllib.request.Request(f"http://{self.server_address}/prompt", data=data)
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())

    def get_image(self, filename, subfolder, folder_type):
        url_values = urllib.parse.urlencode({
            "filename": filename,
            "subfolder": subfolder,
            "type": folder_type
        })
        with urllib.request.urlopen(f"http://{self.server_address}/view?{url_values}") as response:
            return response.read()

    def get_images(self, ws, prompt, client_id):
        res = self.queue_prompt(prompt, client_id)
        prompt_id = res["prompt_id"]
        while True:
            out = ws.recv()
            if isinstance(out, str):
                msg = json.loads(out)
                if msg.get("type") == "executing" and \
                   msg["data"].get("node") is None and \
                   msg["data"].get("prompt_id") == prompt_id:
                    break
        history = self.get_history(prompt_id)[str(prompt_id)]
        output_images = {}
        for node_id, node_output in history["outputs"].items():
            if "images" in node_output:
                imgs = []
                for image in node_output["images"]:
                    img_data = self.get_image(image["filename"], image["subfolder"], image["type"])
                    imgs.append(img_data)
                output_images[node_id] = imgs
        return output_images

    def get_history(self, prompt_id):
        with urllib.request.urlopen(f"http://{self.server_address}/history/{prompt_id}") as response:
            return json.loads(response.read())

    def predict(
        self,
        image1: Path = Input(description="First source image"),
        image2: Path = Input(description="Second source image"),
        image3: Path = Input(description="Third source image"),
        positive_prompt: str = Input(default="a smiling girl", description="Positive text prompt"),
        negative_prompt: str = Input(default="blurry, lowres", description="Negative text prompt"),
        steps: int = Input(default=30, description="Number of diffusion steps"),
        seed: int = Input(default=None, description="Random seed (omit for random)"),
        bypass_reactor: bool = Input(default=False, description="Skip the ReActorFaceSwap node")
    ) -> list[Path]:
        if seed is None:
            seed = int.from_bytes(os.urandom(2), "big")
        client_id = str(uuid.uuid4())
        input_dir = "./ComfyUI/input"
        os.makedirs(input_dir, exist_ok=True)
        for idx, img in enumerate([image1, image2, image3], start=1):
            tgt = os.path.join(input_dir, f"kj{idx}.png")
            SysPath(tgt).write_bytes(open(img, "rb").read())
        wf_path = "./workflow_api/face-match.json"
        with open(wf_path, "r") as f:
            prompt = json.load(f)
        for node in prompt["nodes"]:
            if node.get("id") == 82:
                node["widgets_values"][0] = positive_prompt
            elif node.get("id") == 87:
                node["widgets_values"][0] = negative_prompt
            elif node.get("type") == "RandomNoise":
                node["widgets_values"][0] = seed
                node["widgets_values"][1] = "fixed"
            elif node.get("type") == "ReActorFaceSwap":
                node["widgets_values"][0] = (not bypass_reactor)
        ws = websocket.WebSocket()
        ws.connect(f"ws://{self.server_address}/ws?clientId={client_id}")
        images = self.get_images(ws, prompt, client_id)
        output_dir = "output_images"
        os.makedirs(output_dir, exist_ok=True)
        results = []
        for node_id, imgs in images.items():
            for i, data in enumerate(imgs):
                path = os.path.join(output_dir, f"output_{node_id}_{i}.png")
                Image.open(BytesIO(data)).save(path)
                results.append(Path(path))
                if len(results) >= 2:
                    return results
        return results
