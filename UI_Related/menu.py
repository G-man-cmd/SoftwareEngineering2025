import pygame as py

py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True
FONT = py.font.Font(None, 50)

#input box specifications.
input_box = py.Rect(30, 30, 160, 50)  # Input box dimensions
color_active = py.Color("dodgerblue2")
color_inactive = py.Color("gray")
color = color_inactive

teamR = [""] * 15
teamL = [""] * 15

# Input box dimensions
input_boxes_L = [py.Rect(300, 50 + i * 40, 200, 30) for i in range(15)]  # Left side input fields
input_boxes_R = [py.Rect(690, 50 + i * 40, 200, 30) for i in range(15)]  # Right side input fields

active = False
active_box = None
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
    global active_box

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
                # Check if any input box is clicked
                active_box = None
                for i, box in enumerate(input_boxes_L + input_boxes_R):
                    if box.collidepoint(event.pos):
                        active_box = i
            elif event.type == py.KEYDOWN:
                if active_box is not None:
                    team = teamL if active_box < 15 else teamR
                    index = active_box if active_box < 15 else active_box - 15

                    if event.key == py.K_RETURN:
                        print(f"Player ID Entered: {team[index]}")
                    elif event.key == py.K_BACKSPACE:
                        team[index] = team[index][:-1]  # Remove last character
                    else:
                        team[index] += event.unicode  # Append character

        # Draw input boxes and text
        for i, box in enumerate(input_boxes_L):
            color = color_active if active_box == i else color_inactive
            py.draw.rect(screen, color, box, 2)
            text_surface = FONT.render(teamL[i], True, py.Color("white"))
            screen.blit(text_surface, (box.x + 5, box.y + 5))

        for i, box in enumerate(input_boxes_R):
            color = color_active if active_box == i + 15 else color_inactive
            py.draw.rect(screen, color, box, 2)
            text_surface = FONT.render(teamR[i], True, py.Color("white"))
            screen.blit(text_surface, (box.x + 5, box.y + 5))

        py.display.flip()
        clock.tick(60)
    print(teamL)
    print(teamR)
        
def play_action():
    pass

main_menue()
#game_screen()