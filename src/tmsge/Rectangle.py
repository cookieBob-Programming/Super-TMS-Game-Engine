import pygame
from .Shape import Shape
from .Actor import Actor

class Rectangle(Shape):
    def __init__(self, width: int, height: int, color: tuple[int, int, int]):
        super().__init__(width, height)
        self.color = color

    def tick(self):
        pass
            
    @Actor.only_if_changed
    def draw(self, surface: pygame.Surface, dest: tuple[int, int], area: pygame.Rect = None) -> list[pygame.Rect]:
        
        dest_x, dest_y = dest
        rect = pygame.Rect(dest_x, dest_y, self.width, self.height)
        return [pygame.draw.rect(surface, self.color, rect)]
