# Recommendation System - Multiple Separate Inputs

# Dictionary with categories → items
recommendations = {
    "action": ["Die Hard", "Mad Max", "John Wick"],
    "comedy": ["The Mask", "Friends", "Hera Pheri"],
    "horror": ["Conjuring", "It", "The Ring"],
    "books": ["Harry Potter", "The Alchemist", "Rich Dad Poor Dad"],
    "games": ["Chess", "Valorant", "Among Us"]
}

print("Type a category to get recommendations. Type 'exit' to stop.")

while True:
    category = input("Enter category: ").strip().lower()
    
    if category == "exit":
        print("Thank you! Goodbye.")
        break
    
    if category in recommendations:
        print(f"\nRecommendations for {category}:")
        for item in recommendations[category]:
            print("-", item)
        print()  # blank line for readability
    else:
        print(f"Sorry, no recommendations for '{category}'\n")