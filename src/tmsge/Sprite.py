from .Actor import Actor
from .Costume import Costume
import pygame

class Sprite(Actor):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()

        self.costumes = {}
        self.rect = pygame.Rect(x, y, width, height)
        self.current_costume = None

    @property
    def changed(self):
        return self._changed

    @changed.setter
    def changed(self, value: bool):
        self._changed = value
        if self.current_costume in self.costumes:
            self.costumes[self.current_costume].changed = value

    @property
    def x(self):
        return self.rect.x
    
    @x.setter
    def x(self, value: int):
        if self.rect.x != value:
            self.changed = True
            self.rect.x = value
    
    @property
    def y(self):
        return self.rect.y
    
    @y.setter
    def y(self, value: int):
        if self.rect.y != value:
            self.changed = True
            self.rect.y = value

    #@property


    def add_costume(self, name: str, costume: Costume):
        self.costumes[name] = costume
        if self.current_costume is None:
            self.current_costume = name

    def tick(self):
        for name in self.costumes:
            self.costumes[name].tick()

    @Actor.only_if_changed
    def draw(self, surface: pygame.Surface, dest: tuple[int, int], area: pygame.Rect = None) -> list[pygame.Rect]:
        rects = []
        if self.current_costume in self.costumes:
            dest_x, dest_y = dest
            dest_x += self.rect.x
            dest_y += self.rect.y
            a = area if area is not None else pygame.Rect(0, 0, self.rect.width, self.rect.height)
            rects.extend(self.costumes[self.current_costume].draw(surface, (dest_x, dest_y), a))
        return rects
