#hat einen sichtbaren effect auf dem spielbildschirm


import pygame
class bob:
    def bob_rede(self,kekse):
        self.kekse = kekse
        print("ich bin bob")
pygame.init()
class Actor(bob):
    '''
        Ein Actor verändert das Aussehen des Spiels = aktives Geschehen
    '''
    

    def tick(self):
        '''
            Etwas passiert
        '''
        pass

    def init(self,actor_x,actor_y,x,y,b,h,sprite):
        self.actor_x = actor_x
        self.actor_y = actor_y
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.sprite = sprite#optional fals actor ein sprite hat


    def draw(self,sprite_x,sprite_y,x,y,b,h,sprite):


        '''
            Gibt ein pygame-Surface dieses Actors zurück
        '''
        pygame.scrn.blit(sprite, (sprite_x, sprite_y), (x, y, b, h))

