from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import Image
from config import Hf_API_KEY


MODELS= ["ByteDance/SDXL-Lightning",

"stabilityai/stable-diffusion-xl-base-1.0",

"stabilityai/sdxl-turbo",

"runwayml/stable-diffusion-v1-5",]

client = InferenceClient(api_key=Hf_API_KEY)

print(f"primary model: {MODELS[0]}")
print("type quit to exit the program \n")

while True:
    prompt = input("enter your prompt: ")
    if prompt.lower() in ["quit", "q", "exit"]:
        print("exiting the program...")
        break
    if not prompt:
        continue
    print("generating")
    image=None
    for model in MODELS:
        try:
            image = client.text_to_image(prompt,model=model)
            break
        except Exception:
            print("executing next model...")
            continue
    if image:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_image_{timestamp}.png"
        image.save(filename)
        print(f"image saved as {filename}")
        image.show()
        print()
    else:
        print("all models failed to generate an image. check your api key")
print("goodbye:")