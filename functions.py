import os

def take_pill(medicine_name):
    if not os.path.exists(f"data/{medicine_name}.txt"):
        return "Medicine not found. Have you created it with [n]New medicine?\n"
    
    file = open(f"data/{medicine_name}.txt", "r")
    read_pills = file.read()

    try:
        current_pills = int(read_pills)
    except ValueError:
        return "Value Error: Couldn't access the number of pills. Check if the data for this medicine is correct.\n"
    
    new_current = current_pills - 1
    with open(f"data/{medicine_name}.txt", "w") as f:
        f.write(f"{new_current}")
    return f"Pill taken. You now have {new_current} pills of {medicine_name} left.\n"

def add_more_meds(medicine_name, count_to_add):
    if not os.path.exists(f"data/{medicine_name}.txt"):
        return "Medicine not found. Have you created it with [n]New medicine?\n"
    
    file = open(f"data/{medicine_name}.txt", "r")
    read_pills = file.read()

    try:
        current_pills = int(read_pills)
    except ValueError:
        return "Value Error: Couldn't access the number of pills. Check if the data for this medicine is correct.\n"
    
    new_current = current_pills + int(count_to_add)
    with open(f"data/{medicine_name}.txt", "w") as f:
        f.write(f"{new_current}")
    return f"Success! You now have {new_current} pills of {medicine_name}.\n"

def delete_medicine(medicine_name):
    if not os.path.exists(f"data/{medicine_name}.txt"):
        return "This medicine doesn't exist in your inventory!\n"
    
    os.remove(f"data/{medicine_name}.txt")
    return "Success! Medicine successfully removed from your inventory.\n"
    
def check_count(): #shows all currently tracked meds
    file_list = os.listdir("data/")
    for med in file_list:    
        remove_txt = med.rstrip(".txt") #This makes only the name of the meds appear to the user, without the file extensions
        file = open(f"data/{med}", "r")
        pills_left = file.read()
        print(f"{remove_txt}: {pills_left} pills left")
        file.close()