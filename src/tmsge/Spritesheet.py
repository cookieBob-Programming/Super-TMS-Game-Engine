class Spritesheet:
    '''
        Represents and loads a spritesheet-file
    '''
<<<<<<< HEAD
    def __init__(self, filename: str, width: int, height: int, columns: int, rows: int, pos_x: int, pos_y: int):
=======
    def __init__(self, filename: str, width: int, height: int, columns: int, rows: int):
>>>>>>> origin/Jonas
        '''
            Parameters:
            filename (str): the full-path location of the spriteshet image file
            width (int): the width of a single sprite
            height (int): the height of a single sprite
            columns (int): the amount of columns in the spritesheet
            rows (int): the amount of rows in the spritesheet
        '''
        self.filename = filename
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.load()
    
    def load(self):
        '''
            Loads the spritesheet
        '''
        pass
