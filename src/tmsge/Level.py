from abc import ABC, abstractmethod
import pygame

from .Actor import Actor

class Level(Actor, ABC):
    def __init__(self):
        super().__init__()

        self.game = None
        self.actors = []
        self.background = None
        self.is_initialized = False

    def add_actor(self, a: Actor):
        self.actors.append(a)
        
    def tick(self):
        if self.background:
            self.background.tick()
        
        for a in self.actors:
            a.tick()

    def draw(self, surface: pygame.Surface, dest: tuple[int, int], area: pygame.Rect = None) -> list[pygame.Rect]:
        rects = []
        if self.background:
            rects.extend(self.background.draw(surface, dest, area))

        for a in self.actors:
            rects.extend(a.draw(surface, dest, area))
        return rects

    @abstractmethod
    def act(self):
        '''
            Das eigentliche Spielgeschehen
        '''
        pass

    @abstractmethod
    def init(self):
        '''
            Initialisierung des Levels
        '''
        pass