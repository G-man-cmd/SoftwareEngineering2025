import pygame as py
py.init

screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True
dt = 0

def query():#gets initial data
    pass

def update():#once game starts constantly checks points
    pass

def play_music():
    pass

def main_menue():
    py.display.set_caption("Main Menu")
    screen.fill("black")

def game_screen():
    py.display.set_caption("Game Screen")
    screen.fill("black")
    