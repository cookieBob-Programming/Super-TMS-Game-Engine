import pygame
import sys
import os
from abc import ABC, abstractmethod


def resource_path(relative_path):
    try:
        base = sys._MEIPASS
    except AttributeError:
        base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base, "..", relative_path)
    return os.path.join(base, relative_path)


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
        self.debug_sound = pygame.mixer.Sound(resource_path("sounds/debug.ogg"))

        self.bg_bottom = None
        self.bg_top = None

    def set_background(self, path, layer="bottom"):
        img = pygame.image.load(path).convert()
        scaled = pygame.transform.scale(img, self.screen.get_size())
        if layer == "top":
            self.bg_top = scaled
        else:
            self.bg_bottom = scaled

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
            if self.bg_bottom:
                self.screen.blit(self.bg_bottom, (0, 0))
            else:
                self.screen.fill((121, 125, 140))

            for obj in self.objects:
                obj.draw(self.screen)

            if self.bg_top:
                self.screen.blit(self.bg_top, (0, 0))

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
    def __init__(self, x, y, sprite, anim_button=pygame.K_SPACE, rows=2, on_cycle_complete=None):
        super().__init__(x, y)

        self.sprite = sprite
        self.anim_button = anim_button
        self.on_cycle_complete = on_cycle_complete

        self.frame_width = 64
        self.frame_height = 64

        self.frames_per_row = 4
        self.rows = rows

        self.anim_active = anim_button == "always"

        self.current_frame = 0
        self.current_row = 0

        self.timer = 0
        self._mouse_was_down = False

    def update(self, dt):

        if self.anim_button == "always":
            pass
        elif self.anim_button in ("ML", "MR"):
            mouse_buttons = pygame.mouse.get_pressed()
            btn_idx = 0 if self.anim_button == "ML" else 2
            mouse_down = mouse_buttons[btn_idx]
            if mouse_down and not self._mouse_was_down:
                if self.hitbox.collidepoint(pygame.mouse.get_pos()):
                    self.anim_active = True
            self._mouse_was_down = mouse_down
        else:
            keys = pygame.key.get_pressed()
            if keys[self.anim_button] and not self.anim_active:
                self.anim_active = True

        if self.anim_active:
            self.timer += dt

            if self.timer >= 0.12:
                self.timer = 0
                self.current_frame += 1

                # nächste Reihe
                if self.current_frame >= self.frames_per_row:
                    self.current_frame = 0
                    self.current_row += 1

                    # zurück zum Anfang
                    if self.current_row >= self.rows:
                        self.current_row = 0
                        if self.anim_button != "always":
                            self.anim_active = False
                        if self.on_cycle_complete:
                            self.on_cycle_complete()

    def draw(self, screen):

        rect = pygame.Rect(
            self.current_frame * self.frame_width,
            self.current_row * self.frame_height,
            self.frame_width,
            self.frame_height
        )

        screen.blit(
            self.sprite.image,
            (self.x, self.y),
            rect
        )

class Button(GameObject):
    def __init__(self, rect, text="", font=None, text_color=(255, 255, 255),
                 bg_color=(100, 100, 100), hover_color=(150, 150, 150),
                 pressed_color=(0, 200, 0), key=None):
        rect = pygame.Rect(rect)
        super().__init__(rect.x, rect.y)
        self.hitbox_width = rect.width
        self.hitbox_height = rect.height
        self.hitbox = rect.copy()
        self.update_hitbox()

        self.text = text
        self.font = font or pygame.font.Font(None, 36)
        self.text_color = text_color
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.pressed_color = pressed_color
        self.key = key

        self._was_held = False
        self._clicked = False
        self._is_pressed = False

    def update(self, dt):
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        hovering = self.hitbox.collidepoint(mouse_pos)

        self._is_pressed = hovering and mouse_pressed

        if self.key:
            keys = pygame.key.get_pressed()
            if keys[self.key]:
                self._is_pressed = True

        self._clicked = False
        if self._is_pressed:
            self._was_held = True
        elif self._was_held and hovering:
            self._clicked = True
            self._was_held = False
        else:
            self._was_held = False

    def pressed(self):
        return self._clicked

    def draw(self, screen):
        if self._is_pressed:
            color = self.pressed_color
        elif self.hitbox.collidepoint(pygame.mouse.get_pos()):
            color = self.hover_color
        else:
            color = self.bg_color

        pygame.draw.rect(screen, color, self.hitbox)
        pygame.draw.rect(screen, (0, 0, 0), self.hitbox, 2)

        if self.text:
            text_surf = self.font.render(self.text, True, self.text_color)
            text_rect = text_surf.get_rect(center=self.hitbox.center)
            screen.blit(text_surf, text_rect)

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
