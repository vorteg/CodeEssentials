from game_functions import load_image, scroll_art_ascill, print_title

def initial_screen():
    # De aqui se ejecuta las tareas iniciales del juego
    #image = load_image("opening_image.txt")
    #scroll_art_ascill(image)
    title = print_title()
    scroll_art_ascill(title)
    opening_question = "\n ¿Iniciar partida? (Si/No):" 
    
    while True:
        answer = input(opening_question).lower()

        if answer == "si":
            print("Cargando primer nivel...")
            return
        elif answer == "no":
            print("¡Juego terminado! Hasta luego.")
            exit()
        else:
            print("Respuesta no válida. Por favor, introduce 'Si' o 'No'.")
