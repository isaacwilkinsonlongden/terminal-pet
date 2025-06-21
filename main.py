from pet import Pet


def main():
    pet_name = input("Enter your pet's name: ")
    pet = Pet(pet_name, 5, 5, 5)

    while True:
        action = input("Feed, play, rest, or status? ").strip().lower()
        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "rest":
            pet.rest()
        elif action == "status":
            pet.status()
        elif action == "quit":
            break


if __name__ == "__main__":
    main()
