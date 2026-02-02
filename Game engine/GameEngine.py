import tkinter as tk
from tkinter import filedialog
import pygame


pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()


#bild pfad
sprite = filedialog.askopenfilename(
    title="Sprite auswählen",
    filetypes=[
        ("Bilddateien", "*.png *.jpg *.jpeg")])

#background Musik

background_musik_path = "sounds/title_origin.mp3"
debugsound_musik_path = "sounds/debug.mp3"

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
sprite_hitbox = pygame.Rect(sprite_x+16, sprite_y+48, 32, 16)
npc_hitbox = pygame.Rect(npc_x+16, npc_y+48, 32, 16)

#debug
debug = True


touch = False
allow_window = False


speed = 3 #sprite speed
ticks_per_frame = 40


scrn = pygame.display.set_mode((dx, dy))



pygame.display.set_caption("Super-TMS-Game Engine")
sprite = pygame.image.load(sprite).convert_alpha()
npc = pygame.image.load(npc).convert_alpha()

pygame.mixer.music.load(background_musik_path)
pygame.mixer.music.play(loops=-1)



status = True
while status:
    # background
    scrn.fill([0, 128, 0])



    scrn.blit(npc, (npc_x, npc_y), (npc_sprite_x, npc_sprite_y, b, h))
    scrn.blit(sprite, (sprite_x, sprite_y), (x,y,b,h))

    #debug
    if debug:
        pygame.draw.rect(scrn, (255, 0, 0), sprite_hitbox, 1)
        pygame.draw.rect(scrn, (0, 0, 255), npc_hitbox, 1)






                    # hitbox update
    sprite_hitbox.x = sprite_x+16
    sprite_hitbox.y = sprite_y+48

    npc_hitbox.x = npc_x+16
    npc_hitbox.y = npc_y+48

    # collision check
    if sprite_hitbox.colliderect(npc_hitbox):
        touch = True
    else:
        touch = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    if touch and allow_window:
        allow_window = False
        root = tk.Tk()
        root.title("Info")
        label = tk.Label(root, text="Willkommen zu meinem super tollem menü!")
        label.pack()
        root.mainloop()

    elif not touch and not allow_window:
        allow_window = True



    #movemnt
    if event.type == pygame.KEYDOWN:



        if event.key == pygame.K_LEFT:
            y = 64
            x = (x + 64) % 256
            pygame.time.wait(ticks_per_frame)
            sprite_x -= speed
        elif event.key == pygame.K_DOWN:
            y = 0
            x = (x + 64) % 256
            pygame.time.wait(ticks_per_frame)
            sprite_y += speed
        elif event.key == pygame.K_RIGHT:
            y = 128
            x = (x + 64) % 256
            pygame.time.wait(ticks_per_frame)
            sprite_x += speed
        elif event.key == pygame.K_UP:
            y = 192
            x = (x + 64) % 256
            pygame.time.wait(ticks_per_frame)
            sprite_y -= speed
        elif event.key == pygame.K_F9:
            debug = not debug

            print(touch)
            #Debug Sound
            debug_sound = pygame.mixer.Sound(debugsound_musik_path)
            debug_sound.play()



    pygame.display.flip()
    clock.tick(60)




pygame.quit()