from opening_screen import initial_screen
from game_functions import load_bar,clean_screen

def main():
    initial_screen()
    load_bar()
    clean_screen()
    player_record = level_manager()

if __name__ == "__main__":
    main()
