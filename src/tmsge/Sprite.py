from .Element import Element
from .Costume import Costume

class Sprite(Element):
    def __init__(self):
        self.costumes = {}
    
    def add_costume(self, name: str, costume: Costume):
        self.costumes[name] = costume    

    def tick(self):
        for name in self.costumes:
            self.costumes[name].tick()
