import pygame

pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("My Screen")

running = True
while running:
    mouse = pygame.mouse.get_pos()

    khonekh_button = pygame.Rect(300, 150, 140, 60)
    teacher_button = pygame.Rect(300, 240, 140, 60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # Dark background
    pygame.display.flip()

pygame.quit()
#
# 2. PyQt5 / PySide6 (Advanced, professional GUIs)
#
# Feature-rich, supports complex layouts, widgets, and styling.
# Install:Bashpip install PyQt5
#
#
# Example:
#
# Pythonfrom PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
# import sys
#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle("My Screen")
# window.resize(400, 300)
#
# layout = QVBoxLayout()
# layout.addWidget(QLabel("Hello, this is my screen!"))
# window.setLayout(layout)
#
# window.show()
# sys.exit(app.exec_())
#
#
# 3. Pygame (For games or full-screen graphics)
#
# Ideal for creating custom-drawn screens, animations, and games.
# Install:Bashpip install pygame
#
#
# Example:
#
# Pythonimport pygame
#
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("My Screen")
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((30, 30, 30))  # Dark background
#     pygame.display.flip()
#
# pygame.quit()

