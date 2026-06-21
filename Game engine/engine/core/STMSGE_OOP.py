import pygame
from abc import ABC, abstractmethod


# -----------------------------
# BASE OBJECT
# -----------------------------

class GameObject(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Hitbox (Standard)
        self.hitbox_offset_x = 0
        self.hitbox_offset_y = 0
        self.hitbox_width = 32
        self.hitbox_height = 32

        self.hitbox = pygame.Rect(
            int(self.x),
            int(self.y),
            self.hitbox_width,
            self.hitbox_height
        )

        self.update_hitbox()

    def update_hitbox(self):
        self.hitbox.x = int(self.x + self.hitbox_offset_x)
        self.hitbox.y = int(self.y + self.hitbox_offset_y)

    def touch(self, other):
        return self.hitbox.colliderect(other.hitbox)

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self, screen):
        pass


# -----------------------------
# ENGINE
# -----------------------------

class Engine:
    def __init__(self, width=800, height=600, title="STMSGE Engine"):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.running = True
        self.objects = []

        self.debug = False
        self.debug_sound = pygame.mixer.Sound("../sounds/debug.ogg")

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)

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

            # UPDATE
            for obj in self.objects:
                obj.update(dt)
                obj.update_hitbox()

            # DRAW
            self.screen.fill((30, 30, 30))

            for obj in self.objects:
                obj.draw(self.screen)

            # DEBUG HITBOXES
            if self.debug:
                for obj in self.objects:
                    pygame.draw.rect(self.screen, (255, 0, 0), obj.hitbox, 1)

            pygame.display.flip()

        pygame.quit()


# -----------------------------
# SPRITE
# -----------------------------

class Sprite:
    def __init__(self, path):
        self.image = pygame.image.load(path).convert_alpha()


# -----------------------------
# MUSIC / SOUND
# -----------------------------

class Music:
    def load(self, path):
        pygame.mixer.music.load(path)

    def play(self, loop=-1):
        pygame.mixer.music.play(loop)


class Sound:
    def __init__(self, path):
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        self.sound.play()


# -----------------------------
# ANIMATION
# -----------------------------

class SimpleAnimation:
    def __init__(self, frame_w, frame_h, max_frames, speed=0.15):
        self.frame_w = frame_w
        self.frame_h = frame_h
        self.max_frames = max_frames
        self.speed = speed

        self.timer = 0
        self.frame = 0
        self.row = 0

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.speed:
            self.timer = 0
            self.frame = (self.frame + 1) % self.max_frames

    def get_rect(self):
        return (
            self.frame * self.frame_w,
            self.row,
            self.frame_w,
            self.frame_h
        )

    def set_row(self, row):
        self.row = row


# -----------------------------
# PLAYER
# -----------------------------

class Player(GameObject):
    def __init__(self, x, y, sprite, speed=200, controls=None):
        super().__init__(x, y)

        self.sprite = sprite
        self.speed = speed

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
            self.anim.frame = 0

    def draw(self, screen):
        screen.blit(
            self.sprite.image,
            (self.x, self.y),
            self.anim.get_rect()
        )


# -----------------------------
# NPC
# -----------------------------

class NPC(GameObject):
    def __init__(self, x, y, sprite):
        super().__init__(x, y)
        self.sprite = sprite

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.sprite.image, (self.x, self.y))

class Button:
    def __init__(self, rect, key=None):
        self.rect = pygame.Rect(rect)
        self.key = key
        self._pressed = False

    def update(self):
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        self._pressed = self.rect.collidepoint(mouse_pos) and mouse[0]

        # optional keyboard binding
        if self.key:
            keys = pygame.key.get_pressed()
            if keys[self.key]:
                self._pressed = True

    def pressed(self):
        return self._pressed

    def draw(self, screen):
        color = (0, 200, 0) if self._pressed else (100, 100, 100)
        pygame.draw.rect(screen, color, self.rect)

class OSD:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.messages = []

    def add(self, text, duration=2.0, color=(255,255,255)):
        self.messages.append({
            "text": text,
            "time": duration,
            "color": color
        })

    def update(self, dt):
        for msg in self.messages:
            msg["time"] -= dt

        self.messages = [m for m in self.messages if m["time"] > 0]

    def draw(self, screen):
        y = 10
        for msg in self.messages:
            img = self.font.render(msg["text"], True, msg["color"])
            screen.blit(img, (10, y))
            y += 25