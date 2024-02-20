import time
import os
from colorama import Fore, Style
from pyfiglet import figlet_format

def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def scroll_art_ascill(art_ascii):
    lines = art_ascii.split("\n")
    for line in range(len(lines) + 1):
        clean_screen()
        print(Fore.CYAN + "\n".join(lines[:line]) + Style.RESET_ALL)
        time.sleep(0.2)

def load_image(image_file):
    with open(image_file, "r") as file:
        img = file.read()
    return img

def print_title():
    title = figlet_format("Digitos Mortales")
    return Fore.RED + title + Style.RESET_ALL