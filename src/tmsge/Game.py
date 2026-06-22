from .Level import Level
import pygame
class Game:
    def __init__(self, width: int, height: int, name: str = "Super TMS Game Engine"):
        self.name = name
        self.window = self.create_window(width, height)
        self.levels = []
        self.current_level_index = None
       
        
    def add_level(self, level: Level):
        level.game = self
        self.levels.append(level)
        if self.current_level_index is None:
            self.current_level_index = 0
    
    def create_window(self, width: int, height: int):
        if width > 0 and height > 0:
                self.scrn = pygame.display.set_mode((width, height))
                pygame.display.set_caption(self.name)
                return self.scrn
        
    def run(self):
        if self.current_level_index is not None:
            while True:
                self.levels[self.current_level_index].tick()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
    def get_events():
        return pygame.event.get()
                
