import requests

api_url="https://uselessfacts.jsph.pl/random.json?language=en"

def get_rand_facts():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return print(f"did you know? {data['text']}")
    else:
        return print("Failed to retrieve facts. Please try again later.")
while True:
    user_input = input("press enter to get a random fact or type 'q' to exit")
    if user_input.lower() == "q":
        print("Exiting the program. Goodbye!")
        break
    get_rand_facts()