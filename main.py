import os
from owner import Owner
from pet import Pet


def main():
    clear()
    owner_name = input("Enter your name: ")
    pet_name = input("Enter your pet's name: ")
    pet = Pet(pet_name, 5, 5, 5)
    owner = Owner(owner_name, pet)

    while True:
        clear()
        action = input("inventory, interact, or adventure? ").strip().lower()
        if action == "inventory":
            clear()
            owner.show_inventory()
            input("Press ENTER to return")
        elif action == "interact":
            clear()
            pet_action = input("Feed, play, rest, or status? ").strip().lower()
            if pet_action == "feed":
                owner.give_item("food")
            elif pet_action == "play":
                owner.give_item("toy")
            elif pet_action == "rest":
                pet.rest()
            elif pet_action == "status":
                clear()
                pet.status()
                input("Press ENTER to return")
        elif action == "adventure":
            owner.go_on_adventure()
            input("Press ENTER to return")
        elif action == "quit":
            break


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
