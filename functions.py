import os

def check_count(medicine_name):
    if not os.path.exists(f"data/{medicine_name}.txt"):
        return "Medicine not found. Have you created it with [n]New medicine?\n" #the \n guarantees new paragraphs to make the terminal clearer to the user
    
    file = open(f"data/{medicine_name}.txt", "r")
    pills_left = file.read()
    return f"You have {pills_left} pills of {medicine_name} left\n"

    
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
    