import pygame
from abc import ABC, abstractmethod


def load_sprite(path: str):
    if not path:
        raise ValueError("No sprite path given!")
    return pygame.image.load(path).convert_alpha()


class GameObject(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.debug = False
        self.debug_sound = pygame.mixer.Sound("../sounds/debug.ogg")


        # Offset wie in engine 1
        self.hitbox_offset_x = 16
        self.hitbox_offset_y = 48
        self.hitbox = pygame.Rect(
            int(self.x + self.hitbox_offset_x),
            int(self.y + self.hitbox_offset_y),
            32,
            16
        )

        #self.hitbox = pygame.Rect(0, 0, 32, 16)
        self.update_hitbox()

    def update_hitbox(self):
        self.hitbox.x = int(self.x + self.hitbox_offset_x )
        self.hitbox.y = int(self.y + self.hitbox_offset_y )
        print("HITBOX UPDATE:", self.hitbox_offset_x, self.hitbox_offset_y)


    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self, screen):
        pass
'''

    def update_hitbox(self):
        self.hitbox.x = self.x
        self.hitbox.y = self.y

'''




class Engine:
    def __init__(self, width=800, height=600, title="Game Engine"):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.running = True
        self.objects = []

        # Debug Mode
        self.debug = False
        self.debug_sound = pygame.mixer.Sound("../sounds/debug.ogg")

    def add_object(self, obj):
        self.objects.append(obj)

    def set_icon(self, path):
        icon_surface = pygame.image.load(path)
        pygame.display.set_icon(icon_surface)

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0

            # EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F9:
                        self.debug = not self.debug
                        self.debug_sound.play()

            for obj in self.objects:
                obj.update(dt)
                obj.update_hitbox()

            for i in range(len(self.objects)):
                for j in range(i + 1, len(self.objects)):
                    obj1 = self.objects[i]
                    obj2 = self.objects[j]

                    if obj1.hitbox.colliderect(obj2.hitbox):
                        print("TOUCH!")

            # DRAW
            self.screen.fill((30, 30, 30))

            for obj in self.objects:
                obj.draw(self.screen)

            # DEBUG DRAW (Hitboxen)
            if self.debug:
                for obj in self.objects:
                    pygame.draw.rect(self.screen, (255, 0, 0), obj.hitbox, 1)

            pygame.display.flip()

        pygame.quit()

class Sprite:
    def __init__(self, path: str):
        self.image = pygame.image.load(path).convert_alpha()



class Music:
    def __init__(self):
        pygame.mixer.init()
        self.loaded = False

    def load(self, path: str):
        pygame.mixer.music.load(path)
        self.loaded = True

    def play(self, loop=-1):
        if not self.loaded:
            raise RuntimeError("Music not loaded")
        pygame.mixer.music.play(loop)


class Sound:
    def __init__(self, path: str):
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        self.sound.play()

'''
Ein Event soll alles sein können

zb. ein trigger der ein Sprite verschwinden lässt(zb. bei berührung)

oder ein Baum den mann mit einer taste put machen kann.
'''



class event(GameObject):
    def __init__(self, x, y, sprite):
        pass




class Player(GameObject):
    def __init__(self, x, y, sprite, speed, controls=None):
        super().__init__(x, y)
        self.sprite = sprite
        self.speed = speed

        # Custom Controls (Standard fallback)
        self.controls = controls or {
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "up": pygame.K_UP,
            "down": pygame.K_DOWN
        }


        self.anim = SimpleAnimation(64, 64, 4)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        moving = False

        if keys[self.controls["left"]]:
            self.x -= self.speed * dt
            self.anim.set_row(64)
            moving = True

        if keys[self.controls["right"]]:
            self.x += self.speed * dt
            self.anim.set_row(128)
            moving = True

        if keys[self.controls["up"]]:
            self.y -= self.speed * dt
            self.anim.set_row(192)
            moving = True

        if keys[self.controls["down"]]:
            self.y += self.speed * dt
            self.anim.set_row(0)
            moving = True


        if moving:
            self.anim.update(dt)
        else:
            self.anim.frame = 0  # idle frame

    def draw(self, screen):
        screen.blit(
            self.sprite,
            (self.x, self.y),
            self.anim.get_rect()
        )



class SimpleAnimation:
    def __init__(self, frame_width, frame_height, max_frames, speed=0.15):
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.max_frames = max_frames
        self.speed = speed

        self.timer = 0
        self.frame = 0
        self.row = 0  # ist y

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.speed:
            self.timer = 0
            self.frame = (self.frame + 1) % self.max_frames

    def get_rect(self):
        return (
            self.frame * self.frame_width,  # x
            self.row,                       # y
            self.frame_width,
            self.frame_height
        )

    def set_row(self, row):
        self.row = row



class NPC(GameObject):
    def __init__(self, x, y, sprite, frame_x=0, frame_y=0, w=64, h=64):
        super().__init__(x, y)
        self.sprite = sprite

        # fixed Frame
        self.frame_x = frame_x
        self.frame_y = frame_y
        self.w = w
        self.h = h

        def update(self, dt):
            self.update_hitbox()

            def update_hitbox(self):
                self.hitbox_offset_x = (64 - 32) // 2
                self.hitbox_offset_y = 64 - 16

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(
            self.sprite,
            (self.x, self.y),
            (self.frame_x, self.frame_y, self.w, self.h)
        )


if __name__ == "__main__":
    engine = Engine(800, 600, "STMSGE-OOP")

    player_sprite = Sprite("../Sprites/Costumes/MORPEKO.png")
    npc_sprite = Sprite("../Sprites/Costumes/CHIKORITA.png")

    player = Player(100, 100, player_sprite)
    npc = NPC(300, 200, npc_sprite)

    engine.add_object(player)
    engine.add_object(npc)

    music = Music()
    music.load("../sounds/title_origin.ogg")
    music.play()

    engine.run()

