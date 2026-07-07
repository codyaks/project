import requests
from config import Hf_API_KEY
from colorama import Fore, Style, init

init(autoreset=True)

DEFAULT_MODEL = "google/pegasus-xsum"

def build_api_url(model_name):
    return f"https://api-inference.huggingface.co/models/{model_name}"
def query(payload, model_name=DEFAULT_MODEL):
    api_url= build_api_url(model_name)
    headers = {"Authorization": f"Bearer {Hf_API_KEY}"}
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()
def summarize_text(text, min_length, max_length, model_name=DEFAULT_MODEL):
    payload = {"inputs": text, "parameters": {"min_length": min_length, "max_length": max_length}}
    print(Fore.BLUE + Style.BRIGHT + f"\n????? AI Summarizing with model: {model_name}")
    result = query(payload, model_name=model_name)
    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print(Fore.RED + "❌ Error in summarization response:", result)
        return None
if __name__ == "__main__":

    print(Fore.YELLOW + Style.BRIGHT + "???? Hi there ! what is your name ?")
    user_name = input("Your name: ").strip()

    if not user_name:
        user_name = "User"
    print(Fore.GREEN + Style.BRIGHT + f"welcome {user_name} ! lets give your text some AI magic ✨")
    print(Fore.YELLOW + Style.BRIGHT + "please enter your text to summarize:")
    user_text = input(">> ").strip()
    if not user_text:
            print(Fore.RED + "❌ No text provided. Exiting.")
    else: 
            print(Fore.YELLOW + Style.BRIGHT + "please enter the model name you want to use:")
            model_choice = input(f"modelname - (leave blank for default ): ").strip()
            if not model_choice:
                model_choice = DEFAULT_MODEL
            print(Fore.GREEN + Style.BRIGHT + "/n choose your summarization style:")
            print("1. Standard summary (quick and concise)") 
            print("2. enhanced summary (more detailed and refined)")
            style_choice = input("Enter 1 or 2").strip()
            if style_choice == "2":
                min_length = 80
                max_length = 200
                print(Fore.BLUE+"enhancing summerization process...")
            else:
                min_length = 50
                max_length = 150
                print(Fore.BLUE+"using standard summerization settings...")
            summary = summarize_text(user_text, min_length, max_length, model_name=model_choice)
            if summary:
                print(Fore.GREEN + Style.BRIGHT + f"\n✅ AI Summarized output for {user_name}:")
                print(Fore.CYAN + Style.BRIGHT + summary)

            else:
                print(Fore.RED + "❌ Summarization failed. Please try again.")



