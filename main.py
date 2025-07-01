import medicine
import functions

menu = """
[t] Take pill
[c] Check how many pills are left
[a] Add more pills
[n] New medicine
[h] Help
[q] Quit
"""
print("========Welcome to Pill Counter!========")

while True:
    print("Please select an option:")
    option = input(menu)

    if option == "t":
        print("Which medicine are you taking now?")
        #asks for user input on the name of medicine, choosing from those that were added to their inventory
        #removes one from the total and marks medicine as taken for today
        print("<Medicine name> taken!") #add later the name of the medicine

    
    elif option == "c":
        medicine_to_check = input("Which medicine count would you like to check?")
        pills_left = functions.check_count(medicine_to_check)
        print(pills_left)
        #asks for user input on the name of medicine, choosing from those that were added to their inventory

    elif option == "a":
        print("Which medicine would you like to add more pills of?")
        #asks for user input on the name of medicine, choosing from those that were added to their inventory
        print("How many pills do you want to add to your inventory?")
        #asks for a number input, adding the number to the total of pills from that medicine

    elif option == "n":
        # asks for input and creates a new instance of the medicine class
        new_medicine = input("Please provide the name of the new medicine:")
        time_to_take = input("At which time of day you will take this medicine? Provide just the number, like 15 for 15h: ")
        #if time_to_take not int or > 24:           ADD ERROR MESSAGES LATER
        #    print("Invalid time. Please start again providing the time of day you'll take the medicine")
        starting_pills = input("Finally, how many pills you already have for this medicine? ")
        #if starting_pills not int:
        #    print("Invalid number of pills. Please type only numbers")
        new_medicine = medicine.Medicine(new_medicine, time_to_take, starting_pills)
    
    elif option == "h":
        print("[t] Take pill -- Removes one pill from the total amount and marks the medicine as taken for today")
        print("[c] Check how many pills are left -- Allows you to see how many pills you have left from a certain medicine")
        print("[a] Add more pills -- Adds more pills to your total (for example, when you have bought more)")
        print("[n] New medicine -- Adds a new medicine to be tracked by the app")
        print("[q] Quit - Exits Pill Counter")

    elif option == "q":
        print("Thank you for using Pill Counter! Hope you get better!")
        break

    else:
        print("Invalid option. Please select by typing a letter (non-caps) from one of the menu options above")