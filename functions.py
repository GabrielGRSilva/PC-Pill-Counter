import os

def check_count(medicine_name):
    if not os.path.exists(f"data/{medicine_name}.txt"):
        return "Medicine not found. Have you created it with [n]New medicine?"
    
    file = open(f"data/{medicine_name}.txt", "r")
    pills_left = file.read()
    return f"You have {pills_left} pills of {medicine_name} left"

    
def take_pill(medicine_name):
    if not os.path.exists(f"data/{medicine_name}.txt"):
        return "Medicine not found. Have you created it with [n]New medicine?"
    
    file = open(f"data/{medicine_name}.txt", "r")
    read_pills = file.read()

    try:
        current_pills = int(read_pills)
    except ValueError:
        return "Value Error: Couldn't access the number of pills. Check if the data for this medicine is correct."
    
    new_current = current_pills - 1
    with open(f"data/{medicine_name}.txt", "w") as f:
        f.write(f"{new_current}")
    return f"Pill taken. You now have {new_current} pills of {medicine_name} left."
        