import pygame as py

py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True
FONT = py.font.Font(None, 50)

#input box specifications.
input_box = py.Rect(30, 30, 280, 50)  # Input box dimensions
color_active = py.Color("dodgerblue2")
color_inactive = py.Color("gray")
color = color_inactive

teamR = []
teamL = []

active = False
user_text = ""

def query():#gets initial data
    pass

def update():#once game starts constantly checks points
    pass

def play_music():
    pass

def main_menue():
    image = py.image.load("logo.jpg")
    image = py.transform.scale(image, (1280, 720))
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
    global active, user_text, color

    running = True
    image = py.image.load("PSS.png")
    image = py.transform.scale(image, (1280, 720))
    py.display.set_caption("Player Entry Screen")

    while running:
        screen.fill("black")
        screen.blit(image, (0, 0))

        # Handle events
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN:
                # Check if input box is clicked
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == py.KEYDOWN:
                if active:
                    if event.key == py.K_RETURN:
                        print("Player ID Entered:", user_text)  # Process input
                        user_text = ""  # Clear text after Enter
                    elif event.key == py.K_BACKSPACE:
                        user_text = user_text[:-1]  # Remove last character
                    else:
                        user_text += event.unicode  # Append character

        # **DRAW INPUT BOX**
        py.draw.rect(screen, color, input_box, 2)  # Draw input box border

        # **RENDER TEXT INSIDE INPUT BOX**
        text_surface = FONT.render(user_text, True, py.Color("white"))  # Render input text
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 10))  # Display text
        
        py.display.flip()
        clock.tick(60)
        
def play_action():
    pass

main_menue()
#game_screen()