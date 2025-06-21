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
            print(f"You fed {self.name}.")


    def play(self):
        if self.energy == 0:
            print(f"{self.name} doesn't have enough energy to play!")
        else:
            self.happiness = min(self.happiness + 1, 10)
            self.energy = max(self.energy - 1, 0)
            print(f"You play with {self.name}.")


    def rest(self):
        if self.energy == 10:
            print(f"{self.name} has too much energy to sleep!")
        else:
            self.energy = min(self.energy + 1, 10)
            print(f"You put {self.name} to bed...")


    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Hunger: {self.hunger}\n"
            f"Happiness: {self.happiness}\n"
            f"Energy: {self.energy}"
        )

