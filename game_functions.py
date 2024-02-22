import time
import os
import shutil
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

def load_bar():
    def print_bar(progress):
        bar = "█" * int(progress / 2)
        spaces = " " * (50 - len(bar))
        print(f"\r[{bar}{spaces}] {progress}% Complete", end="", flush=True)

    for i in range(101):
        time.sleep(.1)
        print_bar(i)


def center_text(text):
    console_size = shutil.get_terminal_size()
    width_console = console_size.columns
    left_spaces = abs((width_console - len(text)) // 2)
    spaces = " " * left_spaces
    return  Fore.LIGHTMAGENTA_EX + f"{spaces}{text}" + Style.RESET_ALL

def writing_text(text, speed=0.05):
    for character in text:
        print(Fore.CYAN + character + Style.RESET_ALL, end="", flush=True)
        time.sleep(speed)
    input(
        Fore.LIGHTYELLOW_EX + "\n Presiona Enter para continuar... " + Style.RESET_ALL
    )

def answer_validation(answer):
    answer = (answer.lower)
    correct_options = ["a","b","c"]
    if answer in correct_options:
        return True
    else:
        print("Respuesta no es valida. Debes ingresar 'a', 'b', o 'c'")
        return False
        



if __name__ == "__main__":
    load_bar()