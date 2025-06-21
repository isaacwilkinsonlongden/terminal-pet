class Pet():
    def __init__(self, name, hunger, happiness, energy):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy


    def feed(self):
        if self.hunger == 10:
            print(f"{self.name} is full!")
        else:
            self.hunger = min(self.hunger + 1, 10)


    def play(self):
        if self.energy == 0:
            print(f"{self.name} doesn't have enough energy to play!")
        else:
            self.happiness = min(self.happiness + 1, 10)
            self.energy = max(self.energy - 1, 0)


    def rest(self):
        if self.energy == 10:
            print(f"{self.name} has too much energy to sleep!")
        else:
            self.energy = min(self.energy + 1, 10)


    def status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")

