import shutil
from colorama import Fore, Style

def load_ascii_art(path):
    with open(path, "r") as file:
        return file.read()

def center_text(text):
    width = shutil.get_terminal_size((80, 20)).columns
    return text.center(width)

def draw_game_screen(pet_art, menu_lines):
    """Displays the pet art on the left, menu on the right."""
    pet_lines = pet_art.strip("\n").split("\n")
    max_pet_width = max(len(line) for line in pet_lines)
    padding = 4

    for i in range(max(len(pet_lines), len(menu_lines))):
        pet_part = pet_lines[i] if i < len(pet_lines) else " " * max_pet_width
        menu_part = menu_lines[i] if i < len(menu_lines) else ""
        print(Fore.CYAN + pet_part.ljust(max_pet_width + padding) + Style.RESET_ALL + menu_part)
