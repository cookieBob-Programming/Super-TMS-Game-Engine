from abc import ABC, abstractmethod
import pygame
import functools
from .EventTrigger import EventTrigger

class Actor(ABC, EventTrigger):
    '''
        Ein Actor verändert das Aussehen des Spiels = aktives Geschehen
    '''
    
    def __init__(self):
        super().__init__()
        self._changed = True
        self.rect = None

    @property
    def changed(self):
        return self._changed

    @changed.setter
    def changed(self, value: bool):
        self._changed = value

    @staticmethod
    def only_if_changed(draw_func):
        @functools.wraps(draw_func)
        def wrapper(self, surface: pygame.Surface, dest: tuple[int, int], area: pygame.Rect = None) -> list[pygame.Rect]:
            result = draw_func(self, surface, dest, area)
            if self.changed:
                self.changed = False
                return result
            else:
                return []
        return wrapper

    @abstractmethod
    def tick(self):
        '''
            Etwas passiert
        '''
        pass

    @abstractmethod
    def draw(self, surface: pygame.Surface, dest: tuple[int, int], area: pygame.Rect = None) -> list[pygame.Rect]:
        '''
            Gibt ein pygame-Surface dieses Actors zurück
        '''
        pass

