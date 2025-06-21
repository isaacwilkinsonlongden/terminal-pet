import random
from pet import Pet


class Owner():
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet
        self.inventory = {"food": 2, "toy": 1}


    def show_inventory(self):
        for item in self.inventory:
            print(f"{item}: {self.inventory[item]}")
        input("\nYou check your bag. Press ENTER...")


    def give_item(self, item_type):
        if item_type == "food":
            if self.inventory["food"] > 0:
                self.pet.feed()
                self.inventory["food"] -= 1
            else:
                input("\nYou have no food! Press enter...")
        elif item_type == "toy":
            if self.inventory["toy"] > 0:
                self.pet.play()
            else:
                input("\nYou have no toys! Press enter...") 


    def go_on_adventure(self):
        x = random.randint(1, 3)
        if x == 1:
            self.inventory["food"] += 1 
            print("\nYou gained 1 food!")
        elif x == 2:
            self.inventory["toy"] += 1
            print("\nYou gained 1 toy!")
        else:
            print("\nYou found nothing")
        input("\nYou and your pet explore. Press enter...")


            