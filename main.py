menu = """
[t] Take pill
[c] Check how many pills are left
[a] Add more pills
[h] Help
[q] Quit
"""
print("========Welcome to Pill Counter!"========)

while True:
    print("Please select an option:")
    option = input(menu)

    if option == "t":
        print("Which medicine are you taking now?")
        #asks for user input on the name of medicine, choosing from those that were added to their inventory
        #removes one from the total and marks medicine as taken for today
        print("<Medicine name> taken!") #add later the name of the medicine

    
    elif option == "c":
        print("Which medicine count would you like to check?")
        #asks for user input on the name of medicine, choosing from those that were added to their inventory

    elif option == "a":
        print("Which medicine would you like to add more pills of?")
        #asks for user input on the name of medicine, choosing from those that were added to their inventory
        print("How many pills do you want to add to your inventory?")
        #asks for a number input, adding the number to the total of pills from that medicine
    
    elif option == "h":
        print("[t] Take pill -- Removes one pill from the total amount and marks the medicine as taken for today")
        print("[c] Check how many pills are left -- Allows you to see how many pills you have left from a certain medicine")
        print("[a] Add more pills -- Adds more pills to your total (for example, when you have bought more)")
        print("[q] Quit - Exits Pill Counter")

    elif option == "q":
        print("Thank you for using Pill Counter! Hope you get better!")
        break

    else:
        print("Invalid option. Please select by typing a letter (non-caps) from one of the menu options above")