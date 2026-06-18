import requests

def get_random_joke():
    url="https://official-joke-api.appspot.com/random_joke"
    response= requests.get(url)

    if response.status_code== 200:
        print(f"full json response: {response.json()}")
        joke_data= response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to fetch a joke. Please try again later."
    
def main():
    print("Welcome to ramdom Joke Generator!")
    while True:
        user_input= input("Press Enter to get a random joke or type 'exit' or 'q' to quit: ").strip().lower()
        if user_input in ("q","exit"):
            print("Goodbye!")
            break
        joke= get_random_joke()
        print(joke)
if __name__ == "__main__":
        main()