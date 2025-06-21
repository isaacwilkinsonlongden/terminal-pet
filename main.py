import os
from colorama import init 
from ui import draw_game_screen, load_ascii_art
from owner import Owner
from pet import Pet

# Init colorama
init()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("-----------------------------------------------------------")
    owner_name = input("Enter your name: ")
    print("-----------------------------------------------------------")
    pet_name = input("Enter your pet's name: ")
    pet = Pet(pet_name, 5, 5, 5)
    owner = Owner(owner_name, pet)

    pet_art = load_ascii_art("assets/ascii_dog.txt")
    clear(pet, pet_art)

    while True:
        clear(pet, pet_art)

        choice = input("\nChoose an option: ").strip().lower()

        if choice in ["4", "quit", "q"]:
            break
        elif choice in ["1", "interact"]:
            clear(pet, pet_art)
            pet_action = input("\nFeed, play, rest, or status? ").strip().lower()
            clear(pet, pet_art)
            if pet_action == "feed":
                owner.give_item("food")
            elif pet_action == "play":
                owner.give_item("toy")
            elif pet_action == "rest":
                pet.rest()
            elif pet_action == "status":
                print(pet)
                print("-----------------------------------------------------------")
                input("\nPress enter...")
        elif choice in ["2", "inventory"]:
            clear(pet, pet_art)
            owner.show_inventory()
        elif choice in ["3", "adventure"]:
            clear(pet, pet_art)
            owner.go_on_adventure()


def clear(pet, pet_art):
    os.system('cls' if os.name == 'nt' else 'clear')
    menu = [
        "-----------------------------------------------------------",
        f"{pet.name} Status:",
        f"🍖 Hunger: {pet.hunger}  🎉 Happiness: {pet.happiness}  ⚡ Energy: {pet.energy}",
        "",  # blank line
        "[1] Interact",
        "[2] Inventory",
        "[3] Adventure",
        "[4] Quit",
        "-----------------------------------------------------------"
    ]
    draw_game_screen(pet_art, menu)


if __name__ == "__main__":
    main()
