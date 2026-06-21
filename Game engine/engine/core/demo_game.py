import pygame
import random

# Engine importieren
from STMSGE_OOP import (
    Engine,
    GameObject,
    Player,
    NPC,
    Sprite,
    Sound,
    Music,
    SimpleAnimation
)


# -----------------------------
# POINT (zeigt touch + hitbox)
# -----------------------------
class Point(GameObject):
    def __init__(self):
        super().__init__(0, 0)

        self.radius = 10

        self.respawn()

        # Hitbox für Engine-Kollision
        self.hitbox_width = 20
        self.hitbox_height = 20

    def respawn(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 550)

    def update(self, dt):
        # Hitbox folgt Position
        self.update_hitbox()

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (int(self.x), int(self.y)),
            self.radius
        )


# -----------------------------
# DEMO GAME
# -----------------------------
class DemoGame:
    def __init__(self):

        # ENGINE START
        self.engine = Engine(800, 600, "STMSGE DEMO")

        # ICON (Engine feature)
        # self.engine.set_icon("icon.png")

        # SOUND TEST (Engine feature)
        self.sound = Sound("../sounds/debug.ogg")

        # MUSIC TEST
        self.music = Music()
        self.music.load("../sounds/title_origin.ogg")
        self.music.play()

        # SPRITES
        sprite = Sprite("../Sprites/Costumes/MORPEKO.png")

        # PLAYER 1
        self.player1 = Player(
            100, 100,
            sprite,
            speed=250,
            controls={
                "left": pygame.K_a,
                "right": pygame.K_d,
                "up": pygame.K_w,
                "down": pygame.K_s
            }
        )

        # PLAYER 2
        self.player2 = Player(
            600, 300,
            sprite,
            speed=250
        )

        # NPC (static object)
        self.npc = NPC(400, 200, sprite)

        # POINT (collision object)
        self.point = Point()

        # ADD OBJECTS (Engine feature)
        self.engine.add_object(self.player1)
        self.engine.add_object(self.player2)
        self.engine.add_object(self.npc)
        self.engine.add_object(self.point)

        # SCORE SYSTEM (Game logic)
        self.score1 = 0
        self.score2 = 0

        self.font = pygame.font.Font(None, 40)

    def run(self):

        while self.engine.running:

            dt = self.engine.clock.tick(60) / 1000

            # -----------------------------
            # EVENTS (Engine loop)
            # -----------------------------
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.engine.running = False

                # DEBUG TOGGLE (Engine feature)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F9:
                        self.engine.debug = not self.engine.debug
                        self.sound.play()

            # -----------------------------
            # UPDATE ALL OBJECTS
            # -----------------------------
            for obj in self.engine.objects:
                obj.update(dt)
                obj.update_hitbox()

            # -----------------------------
            # TOUCH SYSTEM (Engine feature)
            # -----------------------------
            if self.player1.touch(self.point):
                if pygame.key.get_pressed()[pygame.K_e]:
                    self.score1 += 1
                    self.point.respawn()

            if self.player2.touch(self.point):
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.score2 += 1
                    self.point.respawn()

            # -----------------------------
            # DRAW
            # -----------------------------
            self.engine.screen.fill((30, 30, 30))

            for obj in self.engine.objects:
                obj.draw(self.engine.screen)

            # SCORE UI
            self.engine.screen.blit(
                self.font.render(f"P1: {self.score1}", True, (255,255,255)),
                (10, 10)
            )

            self.engine.screen.blit(
                self.font.render(f"P2: {self.score2}", True, (255,255,255)),
                (10, 50)
            )

            # DEBUG HITBOXES (Engine feature)
            if self.engine.debug:
                for obj in self.engine.objects:
                    pygame.draw.rect(
                        self.engine.screen,
                        (255, 0, 0),
                        obj.hitbox,
                        1
                    )

            pygame.display.flip()

        pygame.quit()


# START
if __name__ == "__main__":
    DemoGame().run()