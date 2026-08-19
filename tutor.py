#
# import pygame_widgets
# import pygame
# from pygame_widgets.textbox import TextBox
#
# def output():
#     # Get text in the textbox
#     print(lesson.getText())
#
# pygame.init()
# win = pygame.display.set_mode((1000, 600))
#
# lesson = TextBox(win, 100, 100, 800, 80, fontSize=50,
#                   borderColour=(255,204,255), textColour=(0, 200, 0),
#                   onSubmit=output, radius=5, borderThickness=5)
#
# run = True
# while run:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             run = False
#             quit()
#
#     win.fill((255, 255, 255))
#
#     pygame_widgets.update(events)
#     pygame.display.update()
#
#
# # import pygame
#
# import pygame_widgets
# from pygame_widgets.button import Button
#
# # Set up Pygame
# pygame.init()
# win = pygame.display.set_mode((600, 600))
#
# # Creates the button with optional parameters
# button = Button(
#     # Mandatory Parameters
#     win,  # Surface to place button on
#     100,  # X-coordinate of top left corner
#     100,  # Y-coordinate of top left corner
#     300,  # Width
#     150,  # Height
#
#     # Optional Parameters
#     text='Hello',  # Text to display
#     fontSize=50,  # Size of font
#     margin=20,  # Minimum distance between text/image and edge of button
#     inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
#     hoverColour=(150, 0, 0),  # Colour of button when being hovered over
#     pressedColour=(0, 200, 20),  # Colour of button when being clicked
#     radius=20,  # Radius of border corners (leave empty for not curved)
#     onClick=lambda: print('Click')  # Function to call when clicked on
# )
#
# run = True
# while run:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             run = False
#             quit()
#
#     win.fill((255, 255, 255))
#
#     pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
#     pygame.display.update()

# import pygame_widgets
# import pygame
# from pygame_widgets.slider import Slider
# from pygame_widgets.textbox import TextBox
#
# pygame.init()
# win = pygame.display.set_mode((1000, 600))
#
# slider = Slider(win, 100, 100, 800, 40, min=0, max=99, step=1)
# output = TextBox(win, 475, 200, 50, 50, fontSize=30)
#
# output.disable()  # Act as label instead of textbox
#
# run = True
# while run:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             run = False
#             quit()
#
#     win.fill((255, 255, 255))
#
#     output.setText(slider.getValue())

import consts
import pygame_widgets
import pygame
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.textbox import TextBox


pygame.init()
win = pygame.display.set_mode((1200, 840))
def output():
    # Get text in the textbox
    print(lesson.getText())
dropdown = Dropdown(
    win, 120, 10, 100, 50, name='Select lesson',
    choices=consts.SUBJECTS,
    borderRadius=3, colour=pygame.Color('pink'), values=['lesson selected','lesson selected','lesson selected','lesson selected'], direction='down', textHAlign='left'
)
lesson = TextBox(win, 100, 100, 200, 50, fontSize=30,
                  borderColour=(255,204,255), textColour=(0, 0, 0),
                  onSubmit=output, radius=5, borderThickness=5)


def print_value():
    print(dropdown.getSelected())


button = Button(
    win, 10, 10, 100, 50, text='submit', fontSize=30,
    margin=20, inactiveColour=(255,204,255), pressedColour=(0, 255, 0),
    radius=5, onClick=print_value, font=pygame.font.SysFont('arial', 20),
    textVAlign='bottom'
)

run = True
while run:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))

    pygame_widgets.update(events)
    pygame.display.update()

