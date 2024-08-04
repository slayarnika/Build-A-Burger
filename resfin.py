import random
import sys 

# colours r below

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
ResetAll = "\033[0m"



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

# database
users = {}
orders = {}

# registration 
def register(): 
    print("Register new user")
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    if email in users:
        print("User already exists, please log in.")
        return
    users[email] = {"name": name, "password": password}
    print("\033[92mRegistration successful, Welcome to Build A burger  \033[0m")

# log in
def login():
    print("User log in")
    email = input("Enter email: ")
    password = input("Enter password: ") 
    if email in users and users[email]["password"] == password:
        print("\033[92mWelcome back to Build a burger!"+"   \033[0m")
        return email
    else: 
        print("Invalid log in, please try again.")
        return None

def customise_burger():
    print(" \033[91m +  Build your burger")
    buns = ["plain", "sesame", "brioche", "whole wheat", "sourdough", "none"]
    cheese = ["cheddar", "smoked", "swiss", "blue", "mozzerella", "none"]
    toasted = ["lightly", "medium", "well toasted", "fresh"]
    proteins = ["beef patty", "Chicken patty", "vegeterian patty", "egg", "bacon", "none"]
    salads = ["lettuce", "spinach", "carrot", "onion", "tomato", "pickle", "avocado", "none"]
    sauces = ["ketchup", "smokey BBQ", "mustard","mayo", "mint", "none"] 



# menu categpries and ingrediants with their prices; dictionary (using interges)
buns = {"plain": 1.00, "sesame": 1.10, "brioche": 2.00, "whole wheat": 1.30, "sourdough": 1.50, "none": 0.00}

cheese = {"cheddar": 0.20, "smoked": 0.20, "swiss": 0.25, "blue": 1.00, "mozzerella": 0.10, "none": 0.00}

toasted = {"lightly": 0.00, "medium": 0.00, "well toasted": 0.00, "fresh": 0.00}

proteins = {"beef patty": 1.20, "chicken patty": 1.50, "vegetarian patty": 2.00, "egg": 1.00, "bacon": 0.40, "none": 0.00}

salads = {"lettuce": 0.20, "spinach": 0.25, "carrot": 0.20, "onion": 0.20, "tomato": 0.30, "pickle": 0.10, "avocado": 1.30, "none": 0.00}

sauces = {"tomato": 0.10, "smokey BBQ": 0.10, "mustard": 0.10, "mayo": 0.10, "mint": 0.10, "none": 0.00} 




# allows selection of ingrediants (strings)
def multiple_choice(): 
    print("Select your bun:")
    print("select your cheese:")
    print("select toasted option: ")
    print("select your proteins:")
    print("select your salads:")
    print("select your sauces:")

multiple_choice_bread = {
    "1": "plain"
    "2": "sesame" 
    "3": "brioche"
    "4": "whole wheat"
    "5": "sourdough"
    "6": "none"

    "plain": "plain"
    "sesame": "sesame"
    "brioche": "brioche"
    "whole wheat": "whole wheat"
    "sourdough": "soughdough"
    "none": "none" 
}

multiple_choice_cheese = {
    "1": "cheddar"
    "2": "smoked" 
    "3": "swiss"
    "4": "blue"
    "5": "mozzerella"
    "6": "none"

    "cheddar": "cheddar"
    "smoked": "smoked"
    "swiss": "Swiss"
    "blue": "blue"
    "mozzerella": "mozzerella"
    "none": "none"
}

multiple_choice_toasted = {
    "1": "lightly"
    "2": "medium"
    "3": "well toasted"
    "4": "fresh"

    "lightly": "lightly"
    "medium": "medium"
    "well toasted": "well toasted"
    "fresh": "fresh"
}

multiple_choice_proteins = {
    "1": "beef patty"
    "2": "chicken patty"
    "3": "vegetarian patty"
    "4": "egg"
    "5": "bacon"
    "6": "none"

    "beef patty": "beef patty"
    "chicken patty": "chicken patty"
    "vegetarian patty": "vegetarian patty"
    "egg": "egg"
    "bacon": "bacon"
    "none": "none"
}

multiple_choice_salads = {
    "1":"lettuce"
    "2": "spinach"
    "3": "carrot"
    "4": "onion"
    "5": "tomato"
    "6": "pickle"
    "7": "avocado"
    "8": "none"

    "lettuce": "lettuce"
    "spinach": "spinach"
    "carrot": "carrot"
    "onion": "onion"
    "tomato": "tomato"
    "pickle": "pickle"
    "avocado": "avocado"
    "none": "none"
}

multiple_choice_sauces = {
    "1": "tomato"
    "2": "smokey BBQ"
    "3": "mustard"
    "4": "mayo"
    "5": "mint"
    "6": "none"

    "tomato": "tomato"
    "smokey BBQ": "smokey BBQ"
    "mustard": "mustard"
    "mayo": "mayo"
    "mint": "mint"
    "none": "none"
}


multiple_choice_buns = {
    "plain": "plain"
    "sesame": "sesame"
    "brioche": "brioche" # type: ignore
    "whole wheat": "whole wheat"
    "sourdough": "soughdough"
    "none": "none" 

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
}

    


register()
login()
customise_burger()