import os
from colorama import init 
from ui import draw_game_screen, load_ascii_art
from owner import Owner
from pet import Pet

# Init colorama
init()

def main():
    clear()

    pet_art = load_ascii_art("assets/ascii_dog.txt")

    owner_name = input("Enter your name: ")
    pet_name = input("Enter your pet's name: ")
    pet = Pet(pet_name, 5, 5, 5)
    owner = Owner(owner_name, pet)

    while True:
        clear()

        menu = [
            "[1] Interact",
            "[2] Inventory",
            "[3] Adventure",
            "[4] Quit"
        ]
        draw_game_screen(pet_art, menu)

        choice = input("\nChoose an option: ").strip().lower()

        if choice in ["4", "quit", "q"]:
            break
        elif choice in ["1", "interact"]:
            pet_action = input("Feed, play, rest, or status? ").strip().lower()
            if pet_action == "feed":
                owner.give_item("food")
            elif pet_action == "play":
                owner.give_item("toy")
            elif pet_action == "rest":
                pet.rest()
            elif pet_action == "status":
                print(pet)
            input("You interact with your pet. Press ENTER...")
        elif choice in ["2", "inventory"]:
            owner.show_inventory()
            input("You check your bag. Press ENTER...")
        elif choice in ["3", "adventure"]:
            owner.go_on_adventure()
            input("You and your pet explore. Press ENTER...")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
