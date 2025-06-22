import random
from pet import Pet
from minigames.numberGuessing import play_guessing_minigame


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
        print("You and your pet venture into the unknown...")
        input("Press ENTER to continue...")

        success = play_guessing_minigame()

        if success:
            self.inventory["food"] += 1
            print("You gained 1 food!")

            # Chance for rare item
            if random.random() < 0.2:  # 20% chance
                self.inventory["rare gem"] = self.inventory.get("rare gem", 0) + 1
                print("You also found a mysterious rare gem!")
        else:
            print("You return home with only memories...")

        input("\nPress ENTER to return.")



            