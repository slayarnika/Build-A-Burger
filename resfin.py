import random
import sys 

# Colors are below

Default      = "\033[39m"
Black        = "\033[30m"
Red          = "\033[31m"
Green        = "\033[32m"
Yellow       = "\033[33m"
Blue         = "\033[34m"
Magenta      = "\033[35m"
Cyan         = "\033[36m"
LightGray    = "\033[37m"
DarkGray     = "\033[90m"
LightRed     = "\033[91m"
LightGreen   = "\033[92m"
LightYellow  = "\033[93m"
LightBlue    = "\033[94m"
LightMagenta = "\033[95m"
LightCyan    = "\033[96m"
White        = "\033[97m"
ResetAll     = "\033[0m"

title = (
    "\033[93m ____   __ __  ____  _      ___         ____      ____   __ __  ____    ____    ___  ____  \n"
    "|    \\ |  |  ||    || |    |   \\       /    |    |    \\ |  |  ||    \\  /    |  /  _]|    \\ \n"
    "|  o  )|  |  | |  | | |    |    \\     |  o  |    |  o  )|  |  ||  D  )|   __| /  [_ |  D  )\n"
    "|     ||  |  | |  | | |___ |  D  |    |     |    |     ||  |  ||    / |  |  ||    _]|    / \n"
    "|  O  ||  :  | |  | |     ||     |    |  _  |    |  O  ||  :  ||    \\ |  |_ ||   [_ |    \\ \n"
    "|     ||     | |  | |     ||     |    |  |  |    |     ||     ||  .  \\|     ||     ||  .  \\\n"
    "|_____| \\__,_||____||_____||_____|    |__|__|    |_____| \\__,_||__|\\_||___,_||_____||__|\\_|\n  \033[0m"
)

# Print each line separately
print(title) 
print("\033[97m")  # title + title colour

# Database for users and orders
users = {}
orders = {}

# Registration Function
def register(): 
    print("Register new user")
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    if email in users:
        print("User already exists, please log in.")
        return
    users[email] = {"name": name, "password": password}
    print("\033[92mRegistration successful, Welcome to Build A Burger  \033[0m")

# Login Function
def login():
    print("User log in")
    email = input("Enter email: ")
    password = input("Enter password: ") 
    if email in users and users[email]["password"] == password:
        print("\033[92mWelcome back to Build A Burger!\033[0m")
        return email
    else: 
        print("Invalid log in, please try again.")
        return None

# Customising Burger Function
def customise_burger():
    while True:
        print(" \033[91m +  Build your burger")
        
        # User selects ingredients from each category
        selected_buns = select_ingredients("Select your bun:", multiple_choice_buns, buns)
        selected_cheese = select_ingredients("Select your cheese:", multiple_choice_cheese, cheese)
        selected_toasted = select_ingredients("Select toasted option:", multiple_choice_toasted, toasted)
        selected_proteins = select_ingredients("Select your proteins:", multiple_choice_proteins, proteins)
        selected_salads = select_ingredients("Select your salads:", multiple_choice_salads, salads)
        selected_sauces = select_ingredients("Select your sauces:", multiple_choice_sauces, sauces)

        # Validate and clean up the selected ingredients
        def validate_ingredients(ingredients, valid_dict):
            return [item for item in ingredients if item in valid_dict]

        selected_buns = validate_ingredients(selected_buns, buns)
        selected_cheese = validate_ingredients(selected_cheese, cheese)
        selected_toasted = validate_ingredients(selected_toasted, toasted)
        selected_proteins = validate_ingredients(selected_proteins, proteins)
        selected_salads = validate_ingredients(selected_salads, salads)
        selected_sauces = validate_ingredients(selected_sauces, sauces)

        # Calculate total price of the burger
        total_price = (sum(buns[bun] for bun in selected_buns) +
                       sum(cheese[ch] for ch in selected_cheese) +
                       sum(toasted[toast] for toast in selected_toasted) +
                       sum(proteins[prot] for prot in selected_proteins) +
                       sum(salads[salad] for salad in selected_salads) +
                       sum(sauces[sauce] for sauce in selected_sauces))

        # Print out the customized burger and total price
        print("\nYour customised burger:")
        print(f"Buns: {', '.join(selected_buns)} - ${sum(buns[bun] for bun in selected_buns):.2f}")
        print(f"Cheese: {', '.join(selected_cheese)} - ${sum(cheese[ch] for ch in selected_cheese):.2f}")
        print(f"Toasted: {', '.join(selected_toasted)} - ${sum(toasted[toast] for toast in selected_toasted):.2f}")
        print(f"Proteins: {', '.join(selected_proteins)} - ${sum(proteins[prot] for prot in selected_proteins):.2f}")
        print(f"Salads: {', '.join(selected_salads)} - ${sum(salads[salad] for salad in selected_salads):.2f}")
        print(f"Sauces: {', '.join(selected_sauces)} - ${sum(sauces[sauce] for sauce in selected_sauces):.2f}")
        print(f"Total Price: ${total_price:.2f}")

        # Confirm or restart the order process
        confirm = input("\nDo you want to confirm this order? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("\033[92mOrder confirmed! Thank you for your purchase.\033[0m")
            save_receipt(user_email, selected_buns, selected_cheese, selected_toasted, selected_proteins, selected_salads, selected_sauces, total_price)
            break
        else:
            print("\033[91mOrder not confirmed. Restarting order process.\033[0m")

# Menu categories and ingredients with their prices; dictionary (using integers)
buns = {"plain": 1.00, "sesame": 1.10, "brioche": 2.00, "whole wheat": 1.30, "sourdough": 1.50, "none": 0.00}
cheese = {"cheddar": 0.20, "smoked": 0.20, "swiss": 0.25, "blue": 1.00, "mozzerella": 0.10, "none": 0.00}
toasted = {"lightly": 0.00, "medium": 0.00, "well toasted": 0.00, "fresh": 0.00}
proteins = {"beef patty": 1.20, "chicken patty": 1.50, "vegetarian patty": 2.00, "egg": 1.00, "bacon": 0.40, "none": 0.00}
salads = {"lettuce": 0.20, "spinach": 0.25, "carrot": 0.20, "onion": 0.20, "tomato": 0.30, "pickle": 0.10, "avocado": 1.30, "none": 0.00}
sauces = {"tomato": 0.10, "smokey BBQ": 0.10, "mustard": 0.10, "mayo": 0.10, "mint": 0.10, "none": 0.00}

# Function to allow selection of ingredients (strings)
def select_ingredients(prompt, choices, prices):
    selected_items = []
    while True:
        print(prompt)
        for key, value in choices.items():
            print(f"{key}: {value}")
        selection = input("Enter your choice (number): ").strip()
        if selection.isdigit() and int(selection) in range(1, len(choices) + 1):
            selected_items.append(list(choices.values())[int(selection) - 1])
        else:
            print("Invalid selection. Please enter a number corresponding to your choice.")
            continue
        
        # Ask if the user wants to select more from the same category
        while True:
            another = input("Would you like to select another from this category? (yes/no): ").strip().lower()
            if another in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        if another == 'no':
            break

    return selected_items

# Menu options with their choices
multiple_choice_buns = {
    "1": "plain",
    "2": "sesame",
    "3": "brioche",
    "4": "whole wheat",
    "5": "sourdough",
    "6": "none",
}

multiple_choice_cheese = {
    "1": "cheddar",
    "2": "smoked",
    "3": "swiss",
    "4": "blue",
    "5": "mozzerella",
    "6": "none",
}

multiple_choice_toasted = {
    "1": "lightly",
    "2": "medium",
    "3": "well toasted",
    "4": "fresh",
}

multiple_choice_proteins = {
    "1": "beef patty",
    "2": "chicken patty",
    "3": "vegetarian patty",
    "4": "egg",
    "5": "bacon",
    "6": "none",
}

multiple_choice_salads = {
    "1": "lettuce",
    "2": "spinach",
    "3": "carrot",
    "4": "onion",
    "5": "tomato",
    "6": "pickle",
    "7": "avocado",
    "8": "none",
}

multiple_choice_sauces = {
    "1": "ketchup",
    "2": "smokey BBQ",
    "3": "mustard",
    "4": "mayo",
    "5": "mint",
    "6": "none",
}

# Function to save the receipt to a file
def save_receipt(email, selected_buns, selected_cheese, selected_toasted, selected_proteins, selected_salads, selected_sauces, total_price):
    filename = "receipts_bab.txt"
    
    with open(filename, 'a') as file:
        file.write(f"Receipt for {email}\n")
        file.write("="*30 + "\n")
        file.write(f"Buns: {', '.join(selected_buns)} - ${sum(buns[bun] for bun in selected_buns):.2f}\n")
        file.write(f"Cheese: {', '.join(selected_cheese)} - ${sum(cheese[ch] for ch in selected_cheese):.2f}\n")
        file.write(f"Toasted: {', '.join(selected_toasted)} - ${sum(toasted[toast] for toast in selected_toasted):.2f}\n")
        file.write(f"Proteins: {', '.join(selected_proteins)} - ${sum(proteins[prot] for prot in selected_proteins):.2f}\n")
        file.write(f"Salads: {', '.join(selected_salads)} - ${sum(salads[salad] for salad in selected_salads):.2f}\n")
        file.write(f"Sauces: {', '.join(selected_sauces)} - ${sum(sauces[sauce] for sauce in selected_sauces):.2f}\n")
        file.write("="*30 + "\n")
        file.write(f"Total Price: ${total_price:.2f}\n\n")
    
    print(f"\033[92mReceipt saved to {filename}\033[0m")

def main():
    while True:
        print(Red + "Build A Burger" + White)
        print("1. Register")
        print("2. Login")
        print("3. Build your burger")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            global user_email  # Need to declare global to access in customise_burger
            user_email = login()
        elif choice == '3':
            if 'user_email' in globals():
                customise_burger()
            else:
                print("Please login first.")
        elif choice == '4':
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
