from STMSGE_OOP import *
import pygame
import time
import random
class Game:
    def __init__(self):
        self.wind_mult = 1
        self.notified_lvl1 = False
        self.notified_lvl2 = False
        self.notified_lvl3 = False
        self.notified_lvl4 = False
        self.notified_lvl5 = False
        self.notified_lvl6 = False
        self.notified_lvl7 = False
        self.notified_lvl8 = False
        self.b_bought = False
        self.v_bought = False
        self.s_bought = False
        self.n_bought = False
        self.w_bought = False
        self.g_bought = False
        self.a_bought = False
        self.i_bought = False
        free_spots = [274, 420, 174, 420, 74, 420, 474, 420, 574, 420 ]
        self.current_power = 0
        self.sustainability_info = {
            "flower_turbine": "Die Blumen-Turbine nutzt Windenergie dezentral und bringt grüne Energie direkt vor Ort - nachhaltig und platzsparend.",
            "solar": "Solarenergie wandelt Sonnenlicht in Strom um - emissionsfrei, unerschöpflich und eine Säule der Energiewende.",
            "notstrom": "Notstrom aus Pflanzenöl ist eine CO2-neutrale Alternative zu Diesel und sorgt fur nachhaltige Netzstabilitat.",
            "biogas": "Biogas entsteht aus organischen Abfallen - reduziert Methanemissionen und erzeugt klimaneutralen Strom.",
            "windrad": "Windenergie ist effizient und sauber - jedes Windrad versorgt hunderte Haushalte mit Ökostrom.",
            "geotherm": "Geothermie nutzt die Erdwärme für konstante, klimaneutrale Energie - Tag und Nacht, bei jedem Wetter.",
            "wasser": "Wasserkraft liefert zuverlässig saubere Energie seit Generationen - eine der ältesten und grünsten Energiequellen.",
            "infinite_cat": "Die unendliche Energie-Katze steht für eine Zukunft mit sauberer, unerschöpflicher Energie für alle.",
        }
        self.osd_line_length = 80
        self.engine = Engine(900, 700, "Crank It!")
        self.osd = OSD()
        self.engine.set_background(resource_path("Sprites/bg_01.png"))
        crank_sprite = Sprite(resource_path("Sprites/crank_64x.png"))
        windrad_sprite = Sprite(resource_path("Sprites/windrad.png"))
        solar_sprite = Sprite(resource_path("Sprites/solar.png"))
        biogas_sprite = Sprite(resource_path("Sprites/biogas.png"))
        notstrom_sprite = Sprite(resource_path("Sprites/notstrom.png"))
        #ventilator_sprite = ventilator_sprite("./Sprites/ventilator.png")
        wasser_kraftwerk_sprite = Sprite(resource_path("Sprites/wasser.png"))
        geotherm_sprite = Sprite(resource_path("Sprites/geotherm.png"))
        flower_turbine_sprite = Sprite(resource_path("Sprites/flower.png"))
        infinte_cat_sprite = Sprite(resource_path("Sprites/infinite_power_cat.png"))
        #self.ventilator = NPC(274, 420, ventilator_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(0.02, 0.08)))
        self.crank = NPC(434, 520, crank_sprite, anim_button="ML", on_cycle_complete=lambda: self.add_power(1))
        self.windrad_01 = NPC(234, 420, windrad_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(40*self.wind_mult))
        self.solar = NPC(134, 520, solar_sprite, anim_button="always", rows=1, on_cycle_complete=lambda: self.add_power(random.randint(7, 10)))
        self.biogas = NPC(534, 520, biogas_sprite, anim_button="always", rows=4, on_cycle_complete=lambda: self.add_power(random.randint(27, 30)))
        self.notstrom = NPC(634, 520, notstrom_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(17, 20)))
        self.wasser_kraftwerk = NPC(0, 400, wasser_kraftwerk_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(458000, 562000)))
        self.geotherm = NPC(340, 370, geotherm_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(500, 3000)))
        self.flower_turbine = NPC(760, 520, flower_turbine_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(1, 3 )))
        self.infinte_cat = NPC(430, 200, infinte_cat_sprite, anim_button="always", on_cycle_complete=lambda: self.add_power(random.randint(300000000, 400000000)))
        self.btn_buy = Button((370, 650, 200, 50), text="Buy next item", key=pygame.K_RETURN)
        self.engine.add_object(self.btn_buy)
        # self.engine.add_object(self.biogas)
        # self.engine.add_object(self.notstrom)
        # self.engine.add_object(self.solar)
        # self.engine.add_object(self.windrad_01)
        # self.engine.add_object(self.ventilator)
        self.engine.add_object(self.crank)
        # self.engine.add_object(self.akw)
        # self.engine.add_object(self.geotherm)
        # self.engine.add_object(self.infinte_cat)
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 12)
        self.font2 = pygame.font.SysFont("Arial", 20)
        #self.current_power = 9999999999
    def add_power(self, to_add=1):
        self.current_power += to_add

    def _osd_add_info(self, key, duration=6.0, color=(0, 120, 0)):
        text = self.sustainability_info[key]
        while len(text) > self.osd_line_length:
            split = text.rfind(" ", 0, self.osd_line_length + 1)
            if split == -1:
                split = self.osd_line_length
            self.osd.add(text[:split], duration, color)
            text = text[split:].lstrip()
        if text:
            self.osd.add(text, duration, color)

    def run(self):

        while self.engine.running:

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

            self.osd.update(dt)

            # -----------------------------
            # LEVEL CHECKS
            # -----------------------------
            if self.current_power >= 20:
                self.notified_lvl1 = True
            if self.current_power >= 50:
                self.notified_lvl2 = True
            if self.current_power >= 150:
                self.notified_lvl3 = True
            if self.current_power >= 500:
                self.notified_lvl4 = True
            if self.current_power >= 3000:
                self.notified_lvl5 = True
            if self.current_power >= 8000:
                self.notified_lvl6 = True
            if self.current_power >= 50000:
                self.notified_lvl7 = True
            if self.current_power >= 800000000:
                self.notified_lvl8 = True

            # BUY LOGIC
            if self.notified_lvl1 and not self.v_bought:
                if self.btn_buy.pressed():
                    self.v_bought = True
                    self.engine.add_object(self.flower_turbine)
                    self.current_power -= 15
                    self._osd_add_info("flower_turbine")
            elif self.notified_lvl2 and self.v_bought and not self.s_bought:
                if self.btn_buy.pressed() and self.current_power >= 100:
                    self.engine.add_object(self.solar)
                    self.s_bought = True
                    self.current_power -= 100
                    self._osd_add_info("solar")
            elif self.notified_lvl3 and self.s_bought and not self.n_bought:
                if self.btn_buy.pressed() and self.current_power >= 300:
                    self.engine.add_object(self.notstrom)
                    self.n_bought = True
                    self.current_power -= 300
                    self._osd_add_info("notstrom")
            elif self.notified_lvl4 and self.s_bought and not self.b_bought:
                if self.btn_buy.pressed() and self.current_power >= 600:
                    self.engine.add_object(self.biogas)
                    self.b_bought = True
                    self.current_power -= 600
                    self._osd_add_info("biogas")
            elif self.notified_lvl5 and self.b_bought and not self.w_bought:
                if self.btn_buy.pressed() and self.current_power >= 4000:
                    self.engine.add_object(self.windrad_01)
                    self.w_bought = True
                    self.current_power -= 4000
                    self._osd_add_info("windrad")
            elif self.notified_lvl6 and self.w_bought and not self.g_bought:
                if self.btn_buy.pressed() and self.current_power >= 10000:
                    self.engine.add_object(self.geotherm)
                    self.g_bought = True
                    self.current_power -= 10000
                    self._osd_add_info("geotherm")
            elif self.notified_lvl7 and self.g_bought and not self.a_bought:
                if self.btn_buy.pressed() and self.current_power >= 80000:
                    self.engine.add_object(self.wasser_kraftwerk)
                    self.a_bought = True
                    self.current_power -= 80000
                    self._osd_add_info("wasser")
            elif self.notified_lvl8 and self.a_bought and not self.i_bought:
                if self.btn_buy.pressed() and self.current_power >= 10000000000:
                    self.engine.add_object(self.infinte_cat)
                    self.i_bought = True
                    self.current_power -= 10000000000
                    self._osd_add_info("infinite_cat")

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

            # NOTIFICATIONS (nur die höchste anzeigen)
            if self.notified_lvl8:
                self.engine.screen.blit(
                    self.font2.render("Reached Level 8! Unlocked INFINITE POWER CAT! (10000000000kW)", True, (0,0,0)),
                    (200, 60))
            elif self.notified_lvl7:
                self.engine.screen.blit(
                    self.font2.render("Reached Level Hydroelectric Power Plant! Unlocked Nuclear Power Plant! (80000kW)", True, (0,0,0)),
                    (200, 60))
            elif self.notified_lvl6:
                self.engine.screen.blit(
                    self.font2.render("Reached Level 6! Unlocked Geothermal Power Plant! (10000kW)", True, (0,0,0)),
                    (200, 60))
            elif self.notified_lvl5:
                self.engine.screen.blit(
                    self.font2.render("Reached Level 5! Unlocked Wind Turbine! (4000kW)", True, (0,0,0)),
                    (200, 60))
            elif self.notified_lvl4:
                self.engine.screen.blit(
                    self.font2.render("Reached Level 4! Unlocked Biogas Plant! (600kW)", True, (0,0,0)),
                    (200, 60))
            elif self.notified_lvl3:
                self.engine.screen.blit(
                    self.font2.render("Reached Level 3! Unlocked Emergency Power! (300kW)", True, (0,0,0)),
                    (200, 60))
            elif self.notified_lvl2:
                self.engine.screen.blit(
                    self.font2.render("Reached Level 2! Unlocked Solar Panel! (100kW)", True, (0,0,0)),
                    (200, 60))
            elif self.notified_lvl1:
                self.engine.screen.blit(
                    self.font2.render("Reached Level 1! Unlocked Flower Turbine! (15kW)", True, (0,0,0)),
                    (200, 60))

            self.engine.screen.blit(
                self.font.render(f"Current Power (kW): {self.current_power}", True, (0,0,0)),
            (10, 60))

            self.osd.draw(self.engine.screen)

            pygame.display.flip()

if __name__ == "__main__":
    Game().run()



