import os
import pygame

def load_image(directory):
    img_list = []
    files = os.listdir(directory)
    for file in files:
        image = pygame.image.load(f'{directory}/{file}').convert_alpha()
        img_list.append(image)
    return img_list