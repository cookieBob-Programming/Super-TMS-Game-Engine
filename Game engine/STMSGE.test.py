import STMSGE
import pygame
import tkinter as tk


STMSGE.init()

clock = pygame.time.Clock()

window = STMSGE.Window()

scrn = window.size(800, 600)

#background Musik

background_musik_path = "sounds/title_origin.ogg"
debugsound_musik_path = "sounds/debug.ogg"

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
allow_window = True


speed = 5 * 1.0 #sprite speed
ticks_per_frame = 40

window.title("Super TMS Game Engine")
sprite = STMSGE.load_sprite("Sprites/Costumes/MORPEKO.png")
npc = STMSGE.load_sprite(npc)

music = STMSGE.Music()

music.load(background_musik_path)
music.play(-1)

status = True
while status:
    # background
    #scrn.fill([0, 128, 0])

    background = STMSGE.load_background()

    scrn.blit(background, (0, 0))



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



        #movement
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
                sound = Sound()
                debug_sound = sound.load(debugsound_musik_path)
                debug_sound.play()



    pygame.display.flip()
    clock.tick(60)




pygame.quit()
