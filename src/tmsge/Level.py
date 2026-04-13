from abc import ABC, abstractmethod

class Level:
<<<<<<< HEAD
 
    def __init__(self):
        self.elements = []

                
=======
    
    def __init__(self):
        self.elements = []
    
>>>>>>> origin/Jonas
    def add_element(self, e):
        self.elements.append(e)
        
    def tick(self):
        for e in self.elements:
            e.tick()
