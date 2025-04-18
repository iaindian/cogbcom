import json
from urllib import request

# 1) Load your API‑format workflow
with open("face-match-api.json", "r") as f:
    prompt = json.load(f)

# 2) Overwrite the three LoadImage nodes with your filenames
filenames = ["k1.png", "k2.png", "k3.png"]
for node_id, node in prompt.items():
    if node.get("class_type") == "LoadImage":
        if filenames:
            fn = filenames.pop(0)
            node["inputs"]["path"]  = fn
            node["inputs"]["image"] = True
        else:
            break

# 3) Reset your positive / negative CLIP prompts
#    Node "83" is your positive prompt; "88" your negative prompt
if "83" in prompt:
    prompt["83"]["inputs"]["text"] = "masterpiece best quality man"
if "88" in prompt:
    prompt["88"]["inputs"]["text"] = "bad hands"

# 4) Fix all RandomNoise seeds (so you get reproducible outputs)
for node in prompt.values():
    if node.get("class_type") == "RandomNoise":
        node["inputs"]["noise_seed"] = 42424242424242

# 5) (Everything else—including ReActorFaceSwap node 161—remains untouched.)

# 6) Queue it
def queue_prompt(p):
    data = json.dumps({"prompt": p}).encode("utf-8")
    req = request.Request("http://127.0.0.1:8188/prompt", data=data)
    with request.urlopen(req) as res:
        print("Queued, HTTP status:", res.status)

queue_prompt(prompt)
