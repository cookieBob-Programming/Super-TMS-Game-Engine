import tkinter as tk
from tkinter import filedialog
import pygame







pygame.init()
clock = pygame.time.Clock()
#bild pfad
sprite = filedialog.askopenfilename(
    title="Sprite auswählen",
    filetypes=[
        ("Bilddateien", "*.png *.jpg *.jpeg")])





#npc path
npc = "Sprites/Costumes/CHIKORITA.png"


#location from sprite on sprite sheet
x = 0
y = 0

#npc location auf sprite sheet
npc_sprite_x = 0
npc_sprite_y = 0
b = 64 #sprite breite
h = 64 #sprite höhe



#display settings
dx = 640
dy = 640

#spritelocation
sprite_x = 0
sprite_y = 0

#npc location
npc_x = 64
npc_y = 64

# hitboxes
sprite_hitbox = pygame.Rect(sprite_x, sprite_y, 64, 64)
npc_hitbox = pygame.Rect(npc_x, npc_y, 64, 64)



speed = 1 #sprite speed


scrn = pygame.display.set_mode((dx, dy))





pygame.display.set_caption("Super-TMS-Game Engine")
sprite = pygame.image.load(sprite).convert_alpha()
npc = pygame.image.load(npc).convert_alpha()







status = True
while status:
    # background
    scrn.fill([0, 128, 0])

    scrn.blit(npc, (npc_x, npc_y), (npc_sprite_x, npc_sprite_y, b, h))
    scrn.blit(sprite, (sprite_x, sprite_y), (x,y,b,h))

    #debug
    pygame.draw.rect(scrn, (255, 0, 0), sprite_hitbox, 1)
    pygame.draw.rect(scrn, (0, 0, 255), npc_hitbox, 1)

    # hitbox update
    sprite_hitbox.x = sprite_x
    sprite_hitbox.y = sprite_y

    npc_hitbox.x = npc_x
    npc_hitbox.y = npc_y

    # collision check
    if sprite_hitbox.colliderect(npc_hitbox):
        print("touched")

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