from game_functions import load_image, scroll_art_ascill

def initial_screen():
    image = load_image("opening_image.txt")
    scroll_art_ascill(image)