from STMSGE_OOP import *
import pygame
import time
class Game:
    def __init__(self):
        self.engine = Engine(800, 600, "Make the power!")
        crank_sprite = Sprite("/home/luca/Schreibtisch/Projects/Super-TMS-Game-Engine/crank_64x.png")
        windrad_sprite = Sprite("/home/luca/Schreibtisch/Projects/Super-TMS-Game-Engine/windrad.png")
        solar_sprite = Sprite("/home/luca/Schreibtisch/Projects/Super-TMS-Game-Engine/solar.png")
        biogas_sprite = Sprite("/home/luca/Schreibtisch/Projects/Super-TMS-Game-Engine/biogas.png")
        notstrom_sprite = Sprite("/home/luca/Schreibtisch/Projects/Super-TMS-Game-Engine/notstrom.png")
        self.crank = NPC(100, 100, crank_sprite)
        self.windrad = NPC(150, 150, windrad_sprite, anim_button="always")
        self.solar = NPC(200, 200, solar_sprite, anim_button="always")
        self.biogas = NPC(250, 250, biogas_sprite, anim_button="always")
        self.notstrom = NPC(300, 300, notstrom_sprite, anim_button="always")
        self.engine.add_object(self.biogas)
        self.engine.add_object(self.notstrom)
        self.engine.add_object(self.solar)
        self.engine.add_object(self.windrad)
        self.engine.add_object(self.crank)
        self.current_power = 0
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 12)

    def run(self):

        while self.engine.running:

            dt = self.engine.clock.tick(60) / 1000

            # -----------------------------
            # EVENTS (Engine loop)
            # -----------------------------
            for event in pygame.event.get():
    
                if event.type == pygame.QUIT:
                    self.engine.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.current_power += 1
            # -----------------------------
            # UPDATE ALL OBJECTS
            # -----------------------------
            for obj in self.engine.objects:
                obj.update(dt)
                obj.update_hitbox()

            # -----------------------------
            # DRAW
            # -----------------------------
            self.engine.screen.fill((30, 30, 30))

            for obj in self.engine.objects:
                obj.draw(self.engine.screen)

            self.engine.screen.blit(
                self.font.render(f"Current Power (kWh): {self.current_power}", True, (255,255,255)),
            (10, 50))

            pygame.display.flip()

if __name__ == "__main__":
    Game().run()



