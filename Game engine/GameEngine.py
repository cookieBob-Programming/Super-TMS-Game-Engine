import tkinter as tk
from tkinter import filedialog
import pygame
import time

root = tk.Tk()
root.withdraw()





pygame.init()
clock = pygame.time.Clock()
#bild pfad
sprite = filedialog.askopenfilename(
    title="Sprite auswählen",
    filetypes=[
        ("Bilddateien", "*.png *.jpg *.jpeg")])




#bildrendering
x = 0
y = 0

b = 64 #sprite breite
h = 64 #sprite höhe
#display settings
dx = 256
dy = 256

#spritelocation
sprite_x = 0
sprite_y = 0


speed = 1 #sprite speed


scrn = pygame.display.set_mode((dx, dy))





pygame.display.set_caption('Character animation')
img = pygame.image.load(sprite).convert_alpha()






status = True
while status:
    # background
    scrn.fill([0, 128, 0])



    scrn.blit(img, (sprite_x, sprite_y), (x,y,b,h))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    #movemnt
    if event.type == pygame.KEYDOWN:

        x = (x + 64) % 256

        if event.key == pygame.K_LEFT:
            y = 64
            sprite_x -= speed
        elif event.key == pygame.K_DOWN:
            y = 0
            sprite_y += speed
        elif event.key == pygame.K_RIGHT:
            y = 128
            sprite_x += speed
        elif event.key == pygame.K_UP:
            y = 192
            sprite_y -= speed
    pygame.display.flip()
    clock.tick(60)


pygame.quit()