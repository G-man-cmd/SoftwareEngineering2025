import pygame as py
py.init()

screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True
FONT = py.font.Font(None, 50)
input_box = py.Rect(100, 600, 200, 50)  # Position and size
color_active = py.Color("dodgerblue2")
color_inactive = py.Color("gray")
color = color_inactive

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
    global color, user_text, active
    running = True
    py.display.set_caption("Player Entry Screen")
    screen.fill("black")
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == py.KEYDOWN:
                if active:
                    if event.key == py.K_RETURN:
                        print("Entered text:", user_text)  # Print input to console
                        user_text = ""  # Clear input after pressing Enter
                    elif event.key == py.K_BACKSPACE:
                        user_text = user_text[:-1]  # Remove last character
                    else:
                        user_text += event.unicode  # Add typed character

        # Draw text box
        py.draw.rect(screen, color, input_box, 2)

        # Render text
        text_surface = FONT.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
        
        py.display.flip()
        clock.tick(60)
        
    py.quit()

def play_action():
    pass

main_menue()
#game_screen()