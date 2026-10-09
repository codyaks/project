from groq import generate_response

def run_activity():
    print("ZERO-SHOT, ONE-SHOT & FEW-SHOT LEARNING ACTIVITY")

    category = input("Enter a category (e.g., animal, food, city): ").strip()
    item = input(f"Enter a specific {category} to classify: ").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return

    # Zero-shot example
    zero_shot = f"Is {item} a {category}? Answer yes or no."
    print("\n--- ZERO-SHOT LEARNING ---")
    print(f"Response: {generate_response(zero_shot, temperature=0.3, max_tokens=1024)}")

    # One-shot example
    one_shot = f"""Example: Category: fruit Item: apple Answer: Yes, apple is a fruit. 
    Now you try:
    Category: {category}
    Item: {item}
    Answer:"""
    print("\n--- ONE-SHOT LEARNING ---")
    print(f"Response: {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")

    # Few-shot example (kept same as your original prompt format)
    few_shot = f"""Example 1:
    Category: fruit
    Item: apple
    Answer: Yes, apple is a fruit.

    Example 2:
    Category: animal
    Item: dog
    Answer: Yes, dog is an animal.

    Example 3:
    Category: city
    Item: Paris
    Answer: Yes, Paris is a city.

    Now you try:
    Category: {category}
    Item: {item}
    Answer:"""
    print("\n--- FEW-SHOT LEARNING ---")
    print(f"Response: {generate_response(few_shot, temperature=0.3, max_tokens=1024)}")

    # Creative task
    creative_prompt = f"""Write a one-sentence story about the given word.

    Example 1: Word: moon
    Story: The moon winked at the lovers as they shared their first kiss.

    Example 2: Word: river
    Story: The river whispered secrets to the trees as it flowed gently through the forest.

    Example 3: Word: mountain
    Story: The mountain stood tall, guarding the valley below with its silent strength.

    Word: {item}
    Story:"""
    print("\n--- CREATIVE FEW-SHOT EXAMPLE ---")
    print(f"Response: {generate_response(creative_prompt, temperature=0.7, max_tokens=1024)}")

    # Reflection questions
    print("\n--- REFLECTION QUESTIONS ---")
    print("1. How did the responses differ between zero-shot, one-shot, and few-shot?")
    print("2. Which approach gave the most helpful response?")
    print("3. How did the examples influence the model's output?")

if __name__ == "__main__":
    run_activity()
