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


def requires_init(func):
    global _initialized
    def wrapper(*args, **kwargs):
        if not _initialized:
            raise RuntimeError("\033[91mCannot call any other function before init() has been called!\033[0m")
        return func(*args, **kwargs)
    return wrapper




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
        

#pygame.quit()
