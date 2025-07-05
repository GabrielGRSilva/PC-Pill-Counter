import medicine
import functions

#The front menu that shows the available features to the user
#MAKE LIST OF ALL MEDICINE IN INVENTORY!!!!
menu = """
[t] Take pill
[c] Check how many pills are left
[r] Refill medicine inventory with more pills
[a] Add or remove medicine from your list
[h] Help
[q] Quit\n
"""
print("========Welcome to Pill Counter!========")
while True:
    print("Please select an option:")
    option = input(menu).lower() #the lower guarantees the user input works whether they write A or a, for example.

    if option == "t": #removes one from the total and marks medicine as taken for today
        medicine_to_take = input("Which medicine are you taking now?\n") #The \n will make the terminal more organized to receive the input
        print(functions.take_pill(medicine_to_take.upper())) #the upper() function makes all strings UPPERCASE as standard, avoiding errors
    
    elif option == "c": #checks current medicine count from the data folder
        print("Currently tracked medicine:\n")
        functions.check_count()
        print ("\n") #This makes sure the medicine list is an empty line above the next menu

    elif option == "r": #adds more pills, like when the user buys more
        medicine_to_add = input("Which medicine would you like to add more pills of?\n")
        print(functions.check_count(medicine_to_add.upper()))
        count_to_add = input("How many pills would you like to add to the inventory?\n")

        if count_to_add.isdigit() == False:                         #Checks if the user is typing numbers
            print("Invalid number of pills. Please type only positive numbers\n")
        else:
            print(functions.add_more_meds(medicine_to_add.upper(), count_to_add))

    elif option == "a": 
        suboption = input("Do you want to [a]dd a new medicine or [r]emove one from your list?")

        if suboption == "a": #creates new file on the data folder with the new medicine

            new_medicine = input("Please provide the name of the new medicine:\n")
            starting_pills = input("How many pills you already have for this medicine?\n")
            if starting_pills.isdigit() == False:
                print("Invalid number of pills. Please type only numbers\n")
            else:
                new_medicine = medicine.Medicine(new_medicine.upper(), starting_pills)
        
        elif suboption == "r": #removes existing file from inventory

            print("WARNING: This will remove all existing data for the medicine you choose!\n")
            med_to_delete = input("Please provide the name of the medicine you want to delete:\n")
            print(functions.delete_medicine(med_to_delete.upper()))

        else:
            print("Invalid suboption! Choose between [a] (add new medicine) or [r] (remove existing medicine)\n")
    
    elif option == "h": #explains the available commands to the user
        print("[t] Take pill -- Removes one pill from the total amount and marks the medicine as taken for today")
        print("[c] Check how many pills are left -- Allows you to see how many pills you have left from a certain medicine")
        print("[r] Refill medicine inventory with more pills -- Adds more pills to your total (for example, when you have bought more)")
        print("[a] Add or remove medicine from your list -- Adds or remove a new medicine from the app data")
        print("[q] Quit - Exits Pill Counter\n") #\n in the end provides a paragraph after the next menu instance is printed

    elif option == "q":
        print("Thank you for using Pill Counter! Hope you get better!")
        break

    else: #if the user types something that is not on the menu
        print("Invalid option. Please select by typing a letter from one of the menu options above.\n")