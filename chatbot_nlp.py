import re, random
from colorama import Fore, init
init(autoreset=True)

destinations = {"mountain":["Rocky Mountains", "Alps", "Himalayas"],
                "beach":["Maldives", "Bali", "Hawaii"],
                "city":["New York", "Paris", "Tokyo"]}
jokes=["Why don't scientists trust atoms? Because they make up everything!",
       "Why did the scarecrow win an award? Because he was outstanding in his field!",
       "Why don't programmers like nature? It has too many bugs."]
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
            ptint(Fore.CYAN+"bot:- Great! Have a wonderful trip!")
        elif ans=="no":
            print(Fore.CYAN+"bot:- No worries! lets try again.")
            recommend()
        else:
            print(Fore.CYAN+"bot:- I didn't understand that. Let's try again.")
            recommend()
    else:
        print(Fore.CYAN+"bot:- Sorry, I don't have recommendations for that type.")

        show_help()
        