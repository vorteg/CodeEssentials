from level_managment import level_manager
from opening_screen import initial_screen
from game_functions import load_bar,clean_screen,load_data,writing_text, delete_file

def main():
    delete_file("player.json")
    initial_screen()
    load_bar()
    clean_screen()
    player_record = level_manager()
    clean_screen()
    ending = load_data("ending.json")
    if player_record >= 100:
        writing_text(ending["b"])
    elif 50 <= player_record:
        writing_text(ending["a"])
    else:
        writing_text(ending["c"])
    clean_screen()
    writing_text(f"Puntaje final:  {player_record}")    
    

if __name__ == "__main__":
    main()
