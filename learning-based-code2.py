favorite_foods = {}

def learn_favorite_food(person, food):
    favorite_foods[person] = food
    print(f"Got it! I'll remember that {person} likes {food}.")

def recall_favorite_food(person):
    return favorite_foods.get(person, "I don't know their favorite food yet!")

while True:
    action = input("Do you want to teach (t) or ask (a) about a favorite food? (q to quit): ").strip().lower()
    
    if action == 't':
        person = input("Enter the person's name: ").strip().capitalize()
        food = input(f"What is {person}'s favorite food? ").strip().lower()
        learn_favorite_food(person, food)
    
    elif action == 'a':
        person = input("Whose favorite food do you want to know? ").strip().capitalize()
        print(recall_favorite_food(person))
    
    elif action == 'q':
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter 't', 'a', or 'q'.")
