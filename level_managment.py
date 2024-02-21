import json
import time
from colorama import Fore, Style
from game_functions import clean_screen,center_text,writing_text

PLAYER_SYMBOL_TEXT = "[player]"

def load_levels(json_name):
    with open(json_name) as file:
        return json.load(file)
    


    
def load_text(parraf, name_player=""):
    for text in parraf:
        if name_player:
            text = text.replace(PLAYER_SYMBOL_TEXT, name_player)
        writing_text(text)


def intro_level(level):
    load_text(level["voiceOff"])
    load_text(level["npc"])
    for text in level["questions"]:
        print(Fore.RED + text + Style.RESET_ALL)
        return input()


def run_levels(levels, count=1):
    player_name = " "
    player_score = 0
    for key, level in levels.items():
        clean_screen()
        title = level["title"]
        header = center_text(f"--- Nivel {title}")
        print(header)        
        if title == "Intro":
            player_name = intro_level(level)


def level_manager():
    levels = load_levels("levels.json")
    run_levels(levels)

if __name__ == "__main__":
    level_manager()