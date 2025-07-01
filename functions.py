import os

def check_count(medicine_name):
    if not os.path.exists(f"data/{medicine_name}.txt"):
        return "Medicine not found. Have you created it with [n]New medicine?"
    
    file = open(f"data/{medicine_name}.txt", "r")
    line_1 = file.readline() ##Reads the file, but how do I check exactly how many pills are left?
    if "Pills Left" in line_1:
        line_split_1 = line_1.split(':')
        return f'You have{line_split_1[1]}pills of {medicine_name} left' ##Need to fix it to ignore the \n
    
def take_pill(medicine_name):
    if not os.path.exists(f"data/{medicine_name}.txt"):
        return "Medicine not found. Have you created it with [n]New medicine?"
    
        