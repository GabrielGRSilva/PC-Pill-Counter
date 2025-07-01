import os

class Medicine:
    def __init__(self, name, time, initial_count):
        self.name = name
        self.time = time
        self.initial_count = initial_count
        self.create_medicine_file()

    def create_medicine_file(self):         #this should create a new file to store info for a particular medicine
        if os.path.exists(f"data/{self.name}.txt"):
            print(f"========ERROR! This medicine is already being tracked!========")
        else:
            file = open(f"data/{self.name}.txt", "w")
            file.write(f"Pills Left:{self.initial_count}\n")
            file.write(f"Daily Time:{self.time}\n")
            file.close()


##    ; Remaining Pills; Daily Pills used; Time the medication is taken; If the pill was taken today or not yet;