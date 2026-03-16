import tmsge

class Testlevel(tmsge.Level):
    def __init__(self):
        pass
    
    def tick(self):
        print("running")

mygame = tmsge.Game(800,600)
level1 = Testlevel()
mygame.add_level(level1)

mygame.run()
print("Ende!")
#x = [tmsge.Animation(), tmsge.Costume(), tmsge.Element(), tmsge.Game(), tmsge.Level(), tmsge.Sprite(), tmsge.Tile(), tmsge.Tileset()]
