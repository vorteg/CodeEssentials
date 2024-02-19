import time
import os

def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def scroll_art_ascill(art_ascii):
    lines = art_ascii.split("\n")
    for line in range(len(lines) + 1):
        clean_screen()
        print("\n".join(lines[:line]))
        time.sleep(0.2)

def load_image(image_file):
    with open(image_file, "r") as file:
        img = file.read()
    return img