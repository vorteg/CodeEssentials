def load_image(image_file):
    with open(image_file, "r") as file:
        img = file.read()
    return img