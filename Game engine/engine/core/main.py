from STMSGE_OOP import *
import pygame
import time
import random
from plyer import notification
class Game:
    def __init__(self):
        self.wind_mult = 1
        self.notified_lvl1 = False
        self.notified_lvl2 = False
        self.notified_lvl3 = False
        self.notified_lvl4 = False
        self.notified_lvl5 = False
        self.v_bought = False
        self.s_bought = False
        self.n_bought = False
        free_spots = [274, 420, 174, 420, 74, 420, 474, 420, 574, 420 ]
        self.current_power = 0
        self.engine = Engine(800, 600, "Make the power!")
        self.engine.set_background("./Sprites/bg_01.png")
        crank_sprite = Sprite("./Sprites/crank_64x.png")
        windrad_sprite = Sprite("./Sprites/windrad.png")
        solar_sprite = Sprite("./Sprites/solar.png")
        biogas_sprite = Sprite("./Sprites/biogas.png")
        notstrom_sprite = Sprite("./Sprites/notstrom.png")
        #ventilator_sprite = Sprite("./Sprites/ventilator.png")
        akw_sprite = Sprite("./Sprites/akw.png")
        geotherm_sprite = Sprite("./Sprites/geotherm.png")
        flower_turbine_sprite = Sprite("./Sprites/flower.png")
        infinte_cat_sprite = Sprite("./Sprites/infinite_power_cat.png")
        #self.ventilator = NPC(274, 420, ventilator_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(0.02, 0.08)))
        self.crank = NPC(374, 420, crank_sprite, anim_button="ML", on_cycle_complete=lambda: self.add_power(1))
        self.windrad_01 = NPC(174, 320, windrad_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(40*self.wind_mult))
        self.solar = NPC(74, 420, solar_sprite, anim_button="always", rows=1, on_cycle_complete=lambda: self.add_power(random.randint(7, 10)))
        self.biogas = NPC(474, 420, biogas_sprite, anim_button="always", rows=4, on_cycle_complete=lambda: self.add_power(random.randint(27, 30)))
        self.notstrom = NPC(574, 420, notstrom_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(17, 20)))
        self.akw = NPC(570, 280, akw_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(458000, 562000)))
        self.geotherm = NPC(280, 270, geotherm_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(500, 3000)))
        self.flower_turbine = NPC(700, 420, flower_turbine_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(1, 3 )))
        self.infinte_cat = NPC(370, 100, infinte_cat_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(300000000, 400000000)))
        self.btn_buy = Button((310, 550, 200, 50), text="Buy next item", key=pygame.K_RETURN)
        self.engine.add_object(self.btn_buy)
        # self.engine.add_object(self.biogas)
        # self.engine.add_object(self.notstrom)
        # self.engine.add_object(self.solar)
        # self.engine.add_object(self.windrad_01)
        # self.engine.add_object(self.ventilator)
        self.engine.add_object(self.crank)
        # self.engine.add_object(self.akw)
        # self.engine.add_object(self.geotherm)
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 12)

    def add_power(self, to_add=1):
        self.current_power += to_add

    def run(self):

        while self.engine.running:
            

            if self.current_power == 20 or self.current_power > 20:
                if self.notified_lvl1 == False:
                    notification.notify(
                        title="Reached Level 1!",
                        message="Unlocked Flower Turbine!",
                        app_icon="./Sprites/notify.ico",
                        timeout=3
                    )
                    self.notified_lvl1 = True
            
            if self.current_power == 50 or self.current_power > 50:
                if self.notified_lvl2 == False:
                    notification.notify(
                        title="Reached Level 2!",
                        message="Unlocked Solar Panel!",
                        app_icon="./Sprites/notify.ico",
                        timeout=3
                    )
                    self.notified_lvl2 = True


            if self.current_power == 150 or self.current_power > 150:
                if self.notified_lvl3 == False:
                    notification.notify(
                        title="Reached Level 3!",
                        message="Unlocked Emergency Power!",
                        app_icon="./Sprites/notify.ico",
                        timeout=3
                    )
                    self.notified_lvl3 = True
                
            
            #checking if level 1 was Reached
            if self.notified_lvl1 == True and self.v_bought == False:
                if self.btn_buy.pressed():
                    self.v_bought = True
                    self.engine.add_object(self.flower_turbine)
                    self.current_power -= 15
            
            # checking if level 2 was Reached
            elif self.notified_lvl2 == True and self.v_bought == True and self.s_bought == False:
                if self.btn_buy.pressed():
                    self.engine.add_object(self.solar)
                    self.s_bought = True
                    self.current_power -= 40


            # checking if level 3 was Reached
            elif self.notified_lvl3 == True and self.s_bought == True and self.n_bought == False:
                if self.btn_buy.pressed():
                    self.engine.add_object(self.notstrom)
                    self.n_bought = True
                    self.current_power -= 80

            
            dt = self.engine.clock.tick(60) / 1000

            # -----------------------------
            # EVENTS (Engine loop)
            # -----------------------------
            for event in pygame.event.get():
    
                if event.type == pygame.QUIT:
                    self.engine.running = False


            # -----------------------------
            # UPDATE ALL OBJECTS
            # -----------------------------
            for obj in self.engine.objects:
                obj.update(dt)
                obj.update_hitbox()

            # -----------------------------
            # DRAW
            # -----------------------------
            if self.engine.bg_bottom:
                self.engine.screen.blit(self.engine.bg_bottom, (0, 0))
            else:
                self.engine.screen.fill((30, 30, 30))

            for obj in self.engine.objects:
                obj.draw(self.engine.screen)

            if self.engine.bg_top:
                self.engine.screen.blit(self.engine.bg_top, (0, 0))

            self.engine.screen.blit(
                self.font.render(f"Current Power (kW): {self.current_power}", True, (0,0,0)),
            (10, 50))

            pygame.display.flip()

if __name__ == "__main__":
    Game().run()



