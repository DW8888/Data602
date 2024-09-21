""""

Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.

"""
def im_hungry():
    suggestions = {
        1: "Bacon and eggs", 
        2: "Slice of pizza", 
        3: "Steak frites"
    }

    print("Welcome! What would you like?")
    
    options = {
        1: "Breakfast",
        2: "Lunch",
        3: "Dinner"
    }
    
    for i in options:
        print(f"{i}: {options[i]}")

    try:
        selection = int(input("Please enter the number of your selection: "))

        if selection in suggestions:
            print(f"You selected {options[selection]}. I can suggest you order {suggestions[selection]}.")
        else:
            print("Sorry, I can only suggest meals for breakfast, lunch, or dinner.")
    except ValueError:
        print("Please enter a valid number.")

im_hungry()



    
         