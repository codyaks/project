import re, random
from colorama import Fore, init
init(autoreset=True)

destinations = {"mountain":["Rocky Mountains", "Alps", "Himalayas"],
                "beach":["Maldives", "Bali", "Hawaii"],
                "city":["New York", "Paris", "Tokyo"]}
jokes1=["Why don't scientists trust atoms? Because they make up everything!",
       "Why did the scarecrow win an award? Because he was outstanding in his field!","Why don't programmers like nature? It has too many bugs."]
def normalize_input(text):
    return re.sub(r"\s+"," ", text.strip().lower())
def recommend():
    print(Fore.CYAN+"bot:- sure! What type of destination do you preffer? (mountain, beach, city)")
    preference=input(Fore.GREEN+"you:- ")
    preference=normalize_input(preference)
    
    if preference in destinations:
        suggestion=random.choice(destinations[preference])
        print(Fore.CYAN+"bot:- I recommend you to visit "+suggestion)
        print(Fore.CYAN+"bot :- do you like it? (yes/no)")
        ans=input(Fore.GREEN+"you:- ").lower()

        if ans=="yes":
            print(Fore.CYAN+"bot:- Great! Have a wonderful trip!")
        elif ans=="no":
            print(Fore.CYAN+"bot:- No worries! lets try again.")
            recommend()
        else:
            print(Fore.CYAN+"bot:- I didn't understand that. Let's try again.")
            recommend()
    else:
        print(Fore.CYAN+"bot:- Sorry, I don't have recommendations for that type.")

        show_help()
def jokes():
    print(Fore.CYAN+f"travelbot:- Here's a joke for you: {random.choice(jokes1)}")
    show_help()

def show_help():
    print(Fore.CYAN+"travelbot:- I can help you with the following commands:")
    print(Fore.CYAN+"- I can give travel destination recommendations based on your preferences. type-(recommend)")
    print(Fore.CYAN+"- I can tell you a joke to lighten your mood. type-(joke)")
    print(Fore.CYAN+"to exit type exit")

def chat():
    print(Fore.CYAN+"Hi! I'am travelbot. Here to help you")
    name=input(Fore.CYAN+"travelbot:- What's your name? \n"+Fore.GREEN+"you:- ")
    print(Fore.CYAN+f"travelbot:- Nice to meet you, {name}!")
    show_help()

    while True:
        user_input=input(Fore.GREEN+"you:- ")
        user_input=normalize_input(user_input)

        if user_input==("recommend"):
            recommend()
        elif user_input==("joke"):
            jokes()
        elif user_input==("exit"):
            print(Fore.CYAN+"travelbot:- Goodbye! Safe travels!")
            break
        else:
            print(Fore.CYAN+"travelbot:- I'm sorry, I didn't understand that command.")
            

if __name__ == "__main__":
    chat()