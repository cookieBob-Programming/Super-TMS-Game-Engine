import pygame

from .Level import Level

class Game:
    def __init__(self, width: int, height: int):
        pygame.init()
        self.window = self.create_window(width, height)
        
        self.width = width
        self.height = height

        self.levels = []
        self.current_level_index = None
        
        self.last_updated_rects = []
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.dt = 0

    def add_level(self, level: Level):
        level.game = self
        self.levels.append(level)
        if self.current_level_index is None:
            self.current_level_index = 0
    
    def create_window(self, width: int, height: int):
        return pygame.display.set_mode((width, height))
            
    def run(self):
        if self.current_level_index is not None:
            while True:
                self.dt = self.clock.tick(self.fps)
                if not self.levels[self.current_level_index].is_initialized:
                    self.levels[self.current_level_index].init()
                    self.levels[self.current_level_index].is_initialized = True

                self.levels[self.current_level_index].act()
                self.levels[self.current_level_index].tick()
                changed_rects = self.levels[self.current_level_index].draw(self.window, (0,0))
                
                update_rects = changed_rects + self.last_updated_rects
                pygame.display.update(update_rects)
                self.last_updated_rects = changed_rects