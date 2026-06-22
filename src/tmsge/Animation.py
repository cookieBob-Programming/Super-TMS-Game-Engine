from .Costume import Costume
from .Spritesheet import Spritesheet

class Animation(Costume):
    '''
       An animation based on a spritesheet
    '''
    
    def __init__(self, spritesheet: Spritesheet, row: int, col_start: int, col_end: int):
        '''
            Parameters:
            spritesheet (Spritesheet): the spritesheet that is used in this animation
            row (int): the row in the spritesheet with the spites in this animation
            col_start (int): the first image in this animation
            col_end (int): the last image in this animation
        '''
        pass
        
    def tick(self):
        '''
            Tick: next animation step
        '''
        print("animiere...")
