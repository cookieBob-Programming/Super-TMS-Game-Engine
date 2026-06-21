from abc import ABC, abstractmethod
import pygame

from .Actor import Actor
from .EventTrigger import EventTrigger
from .EventType import EventType
from .Event import Event

class Level(Actor, ABC, EventTrigger):
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

        for current_actor in self.actors:
            for check_actor in self.actors:
                if current_actor == check_actor:
                    continue
                if current_actor.rect.colliderect(check_actor.rect):
                    current_actor.process_event(Event(EventType.COLLIDE, {"target": check_actor}))
                    
    def process_event(self, event):
        if event.type == EventType.MOUSEBUTTONDOWN or event.type == EventType.MOUSEBUTTONUP or event.type == EventType.MOUSEMOTION:
            for a in self.actors:
                if a.rect is not None and a.rect.collidepoint(event.pos):
                    a.process_event(event)
        
        super().process_event(event)
        
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
