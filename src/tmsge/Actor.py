from abc import ABC, abstractmethod

class Actor(ABC):
    '''
        Ein Actor verändert das Aussehen des Spiels = aktives Geschehen
    '''
    
    @abstractmethod
    def tick(self):
        '''
            Etwas passiert
        '''
        pass
    
    @abstractmethod
    def draw(self):
        '''
            Gibt ein pygame-Surface dieses Actors zurück
        '''
        pass