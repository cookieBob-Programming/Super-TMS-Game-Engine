from pathlib import Path
import pygame

from .Costume import Costume
from .Actor import Actor

class Image(Costume):
    def __init__(self, image: Path):
        
        self.image = pygame.image.load(image).convert_alpha()
        super().__init__(self.image.get_width(), self.image.get_height())

    def tick(self):
        pass

    @Actor.only_if_changed
    def draw(self, surface: pygame.Surface, dest: tuple[int, int], area: pygame.Rect = None) -> list[pygame.Rect]:
        return [surface.blit(self.image, dest, area)]