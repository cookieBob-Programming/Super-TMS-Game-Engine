from abc import ABC, abstractmethod

class Level:
    
    @abstractmethod
    def tick(self):
        pass
