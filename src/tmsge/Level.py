from abc import ABC, abstractmethod

class Level:
 
    def __init__(self):
        self.elements = []

                
    def add_element(self, e):
        self.elements.append(e)
        
    def tick(self):
        for e in self.elements:
            e.tick()
