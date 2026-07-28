import requests, base64
from config import Hf_API_KEY

API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {"Authorization": f"Bearer {Hf_API_KEY}", "Content-Type": "application/json"}

MODELS = [

"zai-org/GLM-4.5V",

"Qwen/Qwen2.5-VL-72B-Instruct",

"Qwen/Qwen2.5-VL-32B-Instruct",

"google/gemma-3-27b-it",

]
def data_url(b: bytes)-> str:
    return "data:image/jpeg;base64,"+ base64.b64ecode(b).decode("utf-8")
def exact_err(r:requests.Response)-> str:
    try:
        j=r.json
        return j.get("error"{}).get("message")or str(J)
    except Exception:
        return (r.text or"").strip() or r.reason or "request failed"
    
def box(title:str, lines:list[str], icon: str):
    w=max(30, len(title)+4, *(len(x) for x in lines))
    print("\n"+"⌈"+"-"*(w+2)+"⌉")
    print(f"⎮ {icon} {title.ljust(w-2)} ⎮")
    print("├"+"⎻"*(w+2) + "┤")
    for x in lines:
        print(f"⎜ {x.ljust(w)} ⎟")
    print("⎿"+"-"*(w+2)+"⏌\n")
def caption_single_image():
    image_source= input("enter image filename(default: test.jpg) ").strip() or "test.jpg"
    try:
        with open(image_source,"rb") as f:
            img=f.read
    except Exception as e:
        box("file error",[f"could not load {image_source}", f"reason{e}"])
        return
    base={
        "message":[{"role":"user", "content":[{"type": "text", "text":"give a short caption for this image"},{"type":"image_url", "image_url":{"url":data_url(img)}}
        ]
                    }]
    }
