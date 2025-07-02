import os

class Medicine:
    def __init__(self, name, initial_count):
        self.name = name
        self.initial_count = initial_count
        self.create_medicine_file()

    def create_medicine_file(self):         #this should create a new file to store info for a particular medicine
        if os.path.exists(f"data/{self.name}.txt"):
            print(f"========ERROR! This medicine is already being tracked!========")
        else:
            file = open(f"data/{self.name}.txt", "w")
            file.write(self.initial_count)
            file.close()
            print(f"Success! New medicine added: {self.name}")
