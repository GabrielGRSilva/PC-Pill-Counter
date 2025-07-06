import functions
import os

#The front menu that shows the available features to the user
menu = """
[t] Take pill
[c] Check how many pills are left
[r] Refill medicine inventory with more pills
[a] Add or remove medicine from your list
[h] Help
[q] Quit\n
"""
print("========Welcome to Pill Counter!========")

if not os.path.exists("data/"):
    os.makedirs("data/") #Creates the data folder if it doesn't exist
    
while True:
    print("Please select an option:")
    option = input(menu).lower() #the "lower" guarantees the user input works whether they write A or a, for example.

    if option == "t": #removes one from the total and marks medicine as taken for today
        medicine_name = functions.choose_medicine()
        pills_taken = input("How many pills are you taking?")
        if pills_taken.isdigit():
            print(functions.take_pill(medicine_name, pills_taken))
        else:
            print("ERROR! Please choose the NUMBER of the medicine you are taking and a valid number of pills to take.")
    
    elif option == "c": #checks current medicine count from the data folder
        print("Currently tracked medicine:\n")
        functions.show_tracked_medicines()
        print("\n")

    elif option == "r": #adds more pills, like when the user buys more
        print("Currently tracked medicine:\n")
        medicine_name = functions.choose_medicine()
            
        count_to_add = input("How many pills would you like to add to the inventory?\n")

        if count_to_add.isdigit() == False:
            print("Invalid number of pills. Please type only positive numbers\n")
        else:
            print(functions.add_more_meds(medicine_name, count_to_add))

    elif option == "a": 
        suboption = input("Do you want to [a]dd a new medicine or [r]emove one from your list?\n")

        if suboption == "a": #add new med to JSON file

            medicine_name = input("Please provide the name of the new medicine:\n").upper()
            starting_quantity = input("How many pills you already have for this medicine?\n")
            if starting_quantity.isdigit() == False:
                print("Invalid number of pills. Please type only numbers\n")
            else:
                functions.add_new_medicine(medicine_name, starting_quantity)
        
        elif suboption == "r": #removes existing file from data

            print("WARNING: This will remove all existing data for the medicine you choose!\n")
            med_to_delete = input("Please provide the name of the medicine you want to delete:\n")
            print(functions.delete_medicine(med_to_delete.upper()))

        else:
            print("Invalid suboption! Choose between [a] (add new medicine) or [r] (remove existing medicine)\n")
    
    elif option == "h": #explains the available commands to the user
        print("[t] Take pill -- Removes one pill from the total amount it has")
        print("[c] Check how many pills are left -- Allows you to see how many pills of each medicine you have left")
        print("[r] Refill medicine inventory with more pills -- Adds more pills to a medicine (for example, when you have bought more)")
        print("[a] Add or remove medicine from your list -- Adds or remove a medicine from the app data")
        print("[q] Quit - Exits Pill Counter\n") #\n in the end provides a paragraph after the next menu instance is printed

    elif option == "q":
        print("Thank you for using Pill Counter! Hope you get better!")
        break

    else: #if the user types something that is not on the menu
        print("Invalid option. Please select by typing a letter from one of the menu options above.\n")