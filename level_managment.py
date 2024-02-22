import json
import time
from colorama import Fore, Style
from game_functions import clean_screen,center_text,writing_text,answer_validation

PLAYER_SYMBOL_TEXT = "[player]"

def load_levels(json_name):
    with open(json_name) as file:
        return json.load(file)
    


    
def load_text(parraf, name_player=""):
    for text in parraf:
        if name_player:
            text = text.replace(PLAYER_SYMBOL_TEXT, name_player)
        writing_text(text)
        clean_screen()


def boot_level(level):
    load_text(level["voiceOff"])
    load_text(level["npc"])
    for text in level["questions"]:
        print(Fore.RED + text + Style.RESET_ALL)
        return input()
    

def next_levels(level, player_name):
    load_text(level["voiceOff"],name_player=player_name)
    load_text(level["npc"], name_player=player_name)
    for text in level["questions"]:
        text = text.replace(PLAYER_SYMBOL_TEXT,player_name)
        print(Fore.Red + text + Style.RESET_ALL)
    for text in level["answers"]:
        text = text.replace(PLAYER_SYMBOL_TEXT,player_name)
        print(Fore.GREEN + text + Style.RESET_ALL)
    if level["answers"]:
        answer = input()
        while not answer_validation(answer):
            answer = input("Intenta de nuevo, selecciona una de las opciones validas:")
        return answer
    
def get_destiny_description():
    with open("destiny.json") as file:
        return json.load(file)
    

def sum_digts_birthdate(birthdate):
    digits = [int(digit) for digit  in birthdate if digit.isdigit()]

    sum_of_digit = sum(digits)
    
    while sum_of_digit > 10:
        sum_of_digit = sum(int(digit) for digit in str(sum_of_digit))
    
    return str(sum_of_digit)


def get_birthdate():
    while True:
        birthdate = input("Por favor, ingresa tu fecha de nacimiento en numeros (DD/MM/AAAA)") 

        if len(birthdate) == 10 and  birthdate[2] == "/" and birthdate[5] == "/":
            return birthdate
        else:
            print("Formato incorrecto.Por favor , ingresar la fecha en el fromato (DD/MM/AAAA)")  

def write_destiny(player_description):
    data = {
        "user": player_description,
        "voiceOff": "Tu destino se entrelaza con los números, y parece que alguien ha notado tu presencia.",
    }
    with open("player.json", "w") as file:
        json.dump(data, file)

def handle_kiosko_response(answer):

    def handle_case_a():
        birthdate = get_birthdate()
        number =  sum_digts_birthdate(birthdate)
        book = get_destiny_description()
        write_destiny(book[number])
        return 10
    
    def handle_case_b():
        return 20
    
    def handle_case_c():
        return 1

    actions = {"a": handle_case_a, "b": handle_case_b, "c":handle_case_c}
    action = actions.get(answer.lower())

    if action:
        return action()
    else:
        print("Opción no válida. Por favor, elige 'a', 'b' o 'c'.")
        answer = input()
        return handle_kiosko_response(answer)
    
def challenge(number):
    answers = []
    clean_screen()
    with open("challenges.json") as file:
        game =  json.load(file)

    print(center_text("Desafio"))
    writing_text(game[number]["problema"])

    for _ in game[number]["respuesta"][0]:
        answers.append(int(input("ingresa un digito: ")))

    for answ in game[number]["respuesta"]:
        if sorted(answers) == sorted(answ):
            return 50
    return 0

def run_levels(levels, count=1):
    player_name = " "
    player_score = 0
    for key, level in levels.items():
        clean_screen()
        title = level["title"]
        header = center_text(f"--- Nivel {title} ---")
        print(header)        
        if title == "Intro":
            player_name = boot_level(level)
        else:
            answer = next_levels(level, player_name)
            if title == "kiosko":
                player_score =  player_score + handle_kiosko_response(answer)
            else:
                if level["values"]:
                    player_score = player_score + level["values"][answer]
            if count == 1:
                player_score = player_score + challenge(str(count))
                count = count + 1

    return player_score, count



def level_manager():
    levels = load_levels("levels.json")
    run_levels(levels)

if __name__ == "__main__":
    level_manager()