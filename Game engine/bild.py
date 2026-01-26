import tkinter as tk
from tkinter import filedialog
import pygame
import time

root = tk.Tk()
root.withdraw()





pygame.init()
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

scrn = pygame.display.set_mode((dx, dy))


#background
scrn.fill([0, 128, 0])


pygame.display.set_caption('Character animation')
img = pygame.image.load(sprite).convert_alpha()


# sprite position
sprite_x, sprite_y = 0, 0
sprite_speed = 5






status = True
while status:
    time.sleep(0.2)
    x = (x + 64) % 256
    scrn.blit(img, (0, 0), (x,y,b,h))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False


        #movemnt
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sprite_x -= sprite_speed
            elif event.key == pygame.K_RIGHT:
                sprite_x += sprite_speed
            elif event.key == pygame.K_UP:
                sprite_y -= sprite_speed
            elif event.key == pygame.K_DOWN:
                sprite_y += sprite_speed
    pygame.display.flip()


pygame.quit()