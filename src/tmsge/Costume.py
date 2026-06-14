from abc import ABC, abstractmethod
import pygame

from .Actor import Actor

class Costume(Actor, ABC):
    def __init__(self, width: int, height: int):
        super().__init__()
        
        self.width = width
        self.height = height

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def draw(self, surface: pygame.Surface, dest: tuple[int, int], area: pygame.Rect = None) -> list[pygame.Rect]:
        pass
