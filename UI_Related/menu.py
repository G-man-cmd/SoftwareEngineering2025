import pygame as py
py.init()

screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True

def query():#gets initial data
    pass

def update():#once game starts constantly checks points
    pass

def play_music():
    pass

def main_menue():
    image = py.image.load("turtle.png")
    py.display.set_caption("Main Menu")
    screen.fill("black")
    screen.blit(image, (0, 0))

    py.display.flip()
    start_time = py.time.get_ticks()  # Get current time
    while py.time.get_ticks() - start_time < 3000:  # Run loop for 3 seconds
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                return
        clock.tick(60)  # Limit FPS
    game_screen()

def game_screen():
    running = True
    py.display.set_caption("Game Screen")
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
        screen.fill("black")
        
        py.display.flip()
        #clock.tick(60)
    py.quit()

main_menue()
#game_screen()