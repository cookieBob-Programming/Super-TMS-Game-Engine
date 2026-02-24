import tkinter as tk
from tkinter import filedialog
import pygame


warning_was_shown = False
_initialized = False

def init():
    global _initialized
    pygame.init()
    pygame.mixer.init()
    _initialized = True

#init()

def requires_init(func):
    global _initialized
    def wrapper(*args, **kwargs):
        if not _initialized:
            raise RuntimeError("\033[91mCannot call any other function before init() has been called!"\033[0m)
        return func(*args, **kwargs)
    return wrapper


clock = pygame.time.Clock()


#class for creating a window
class Window:
    
    @requires_init
    def __init__(self):
        self.scrn = None

    @requires_init
    def size(self, dx, dy):
        if dx and dy:
            if dx > 0 and dy > 0:
                self.scrn = pygame.display.set_mode((dx, dy))
                return self.scrn
            else:
                raise ValueError("Width and height must be greater than 0!")
        else:
            raise ValueError("Width and height must be given!")
    
    @requires_init
    def title(self, title):
        if title:
            pygame.display.set_caption(title)
        else:
            raise ValueError("Title must be given!")



#funktion for loading sprites
@requires_init
def load_sprite(path_to_sprite):
    if path_to_sprite:
        return pygame.image.load(path_to_sprite).convert_alpha()
    else:
        return pygame.image.load("Sprites/Costumes/MORPEKO.png").convert_alpha()


class Music:
    
    @requires_init
    def __init__(self):
        self.is_loaded = False
    
    @requires_init
    def load(self, path_to_music):
        if not path_to_music:
            raise ValueError("No music path given!")
        pygame.mixer.music.load(path_to_music)
        self.is_loaded = True
    
    @requires_init
    def play(self, loop=-1):
        if not self.is_loaded:
            raise ValueError("No music loaded! Call load() first.")
        pygame.mixer.music.play(loops=loop)
        

class Sound:

    @requires_init
    def __init__(self):
        self.is_loaded = False

    @requires_init
    def load(self, path_to_sound):
        if not path_to_sound:
            raise ValueError("No sound path given!")
        self.Sound = pygame.mixer.Sound(path_to_sound)
        self.is_loaded = True
        return self

    @requires_init
    def play(self):
        self.Sound.play()


window = Window()


scrn = window.size(640, 640) #create_window(640, 640, "Super-TMS-Game Engine")


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

#funktion for loading images as background
@requires_init
def load_background(path="Sprites/Background/standart_green.png"):
    global warning_was_shown
    if path != "Sprites/Background/standart_green.png":
        return pygame.image.load(path).convert_alpha()
  
    elif path == "Sprites/Background/standart_green.png" and warning_was_shown == False:
        root = tk.Tk()
        root.title("Info")
        label = tk.Label(root, text="No background image selected, using standart green background!", fg="red",bg="yellow", anchor='center')
        label.pack()
        root.mainloop()
        warning_was_shown = True
        return pygame.image.load(path).convert()
    
    else:
        return pygame.image.load(path).convert()
        



window.title("Super-TMS-Game Engine")
sprite = load_sprite("Sprites/Costumes/MORPEKO.png")
npc = load_sprite(npc)

music = Music()

music.load(background_musik_path)
music.play(-1)

if __name__ == "__main__":
    status = True
    while status:
        # background
        #scrn.fill([0, 128, 0])

        background = load_background()

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
