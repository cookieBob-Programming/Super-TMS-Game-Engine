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

#start location
strt_x = 0
strt_y = 0

scrn = pygame.display.set_mode((dx, dy))





pygame.display.set_caption('Character animation')
img = pygame.image.load(sprite).convert_alpha()








status = True
while status:
    time.sleep(0.2)
    x = (x + 64) % 256
    # background
    scrn.fill([0, 128, 0])


    scrn.blit(img, (strt_x, strt_y), (x,y,b,h))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False


        #movemnt
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                y = 64

            elif event.key == pygame.K_DOWN:
                y = 0

            elif event.key == pygame.K_RIGHT:
                y = 128

            elif event.key == pygame.K_UP:
                y = 192
    pygame.display.flip()


pygame.quit()