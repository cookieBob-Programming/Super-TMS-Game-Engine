import pygame

from .Image import Image
from .Actor import Actor
class Spritesheet(Image):
    def __init__(self, image, width, height, columns, rows, speed):
        super().__init__(image)
        self.width = width
        self.height = height
        
        self.rows = rows
        self.columns = columns
        
        self.row = 0
        self.column = 0
    
        self.speed = speed
        self.tick_counter = 0
        
        self.running = False
        
    def tick(self):
        if self.running:
            self.tick_counter += 1
            if self.tick_counter == self.speed:
                self.column = (self.column + 1) % self.columns
                self.tick_counter = 0
        
    @Actor.only_if_changed
    def draw(self, surface: pygame.Surface, dest: tuple[int, int], area: pygame.Rect = None) -> list[pygame.Rect]:
        super().draw(surface, dest, (self.column * self.width, self.row * self.height, self.width, self.height))
