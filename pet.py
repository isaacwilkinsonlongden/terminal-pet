class Pet():
    def __init__(self, name, hunger, happiness, energy):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy


    def feed(self):
        if self.hunger == 10:
            input(f"\n{self.name} is full! Press enter...")
        else:
            self.hunger = min(self.hunger + 1, 10)
            input(f"\nYou fed {self.name}. Press enter...")


    def play(self):
        if self.energy == 0:
            input(f"\n{self.name} doesn't have enough energy to play! Press enter...")
        else:
            self.happiness = min(self.happiness + 1, 10)
            self.energy = max(self.energy - 1, 0)
            input(f"\nYou play with {self.name}. press enter...")


    def rest(self):
        if self.energy == 10:
            input(f"\n{self.name} has too much energy to sleep! Press enter...")
        else:
            self.energy = min(self.energy + 1, 10)
            input(f"\nYou put {self.name} to bed. Press enter...")


    def __str__(self):
        return (
            f"\nName: {self.name}\n"
            f"Hunger: {self.hunger}\n"
            f"Happiness: {self.happiness}\n"
            f"Energy: {self.energy}"
        )

