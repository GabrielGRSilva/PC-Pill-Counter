import json

def show_tracked_medicines(): 
    with open("data/medicines.json", "r") as f:
        medicines = json.load(f)

    if not medicines:
        print("No medicines tracked yet. Add them to your data!")
    else:
        print("Tracked medicines:")
        for med, qty in medicines.items():
            print(f"- {med}: {qty} pills")

    f.close() #Close file to avoid problems

def choose_medicine(): #This is a helper function to enable the user to select meds from a list choosing a number
    with open("data/medicines.json", "r") as f:
        medicines = json.load(f)

    if not medicines:
        print("No medicines tracked yet. Add them to your data!")
        f.close()
        return None

    print("Tracked medicines:")
    med_list = list(medicines.keys())
    for i, med in enumerate(med_list):
        print(f"{i + 1} - {med} ({medicines[med]} pills)\n")

    while True:
        try:
            selection = int(input("Select the number of the medicine to select: "))
            if 1 <= selection <= len(med_list):
                f.close()
                return med_list[selection - 1]
            else:
                f.close()
                print("ERROR! Invalid selection! Try again.")
        except ValueError:
            f.close()
            print("ERROR! Please enter a number.")

    
def take_pill(medicine_name, pills_taken):
    with open("data/medicines.json", "r") as f:
       medicines = json.load(f)

    if medicine_name in medicines:
        medicines[medicine_name] -= int(pills_taken)
        with open("data/medicines.json", "w") as f: #Save data to JSON file
            json.dump(medicines, f, indent = 4)
            f.close()
        return f"Sucess! {pills_taken} pill(s) taken. {medicine_name} now has {medicines[medicine_name]} pills remaining."
        
    else:
        f.close()
        return f"ERROR! {medicine_name} isn't currently being tracked! Add it first."

def add_new_medicine(medicine_name, starting_quantity):
    with open("data/medicines.json", "r") as f:
        medicines = json.load(f)

    if medicine_name in medicines:
        f.close()
        print (f"ERROR! {medicine_name} already exists with quantity {medicines[medicine_name]}!")
        return

    medicines[medicine_name] = starting_quantity

    with open("data/medicines.json", "w") as f: #Save data to JSON file
        json.dump(medicines, f, indent = 4)
        f.close()

    print(f"{medicine_name} added with quantity {starting_quantity}")

def add_more_meds(medicine_name, count_to_add): 
    
    with open("data/medicines.json", "r") as f: 
        medicines = json.load(f)

    if medicine_name not in medicines:
        print(f"ERROR! {medicine_name} isn't being tracked yet! Add it first.")
        f.close()
        return

    try:
        count_to_add = int(count_to_add)
    except ValueError:
        return "ERROR! Invalid number of meds to add!\n"
    
    with open("data/medicines.json", "w") as f:
        json.dump(medicines, f, indent=4)
        f.close()
    return f"Success! You now have {medicines[medicine_name]} pills of {medicine_name}.\n"

def delete_medicine(medicine_name):
    with open("data/medicines.json", "r") as f:
        medicines = json.load(f)

    if medicine_name not in medicines:
        return "This medicine doesn't exist in your data!\n"
        
    del medicines[medicine_name]
    with open("data/medicines.json", "w") as f:  # use "w" to overwrite
        json.dump(medicines, f, indent=4)
        f.close()
        
    return f"Success! {medicine_name} successfully removed from your data.\n"
