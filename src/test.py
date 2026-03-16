import tmsge

class Testlevel(tmsge.Level):
    def __init__(self):
        super().__init__()
        spritesheet = tmsge.Spritesheet("blabla.png", 25, 25, 5, 3)
        animation = tmsge.Animation(spritesheet, 0, 4, 1)
        sprite1 = tmsge.Sprite()
        sprite1.add_costume("animation", animation)
        self.add_element(sprite1)

mygame = tmsge.Game(800,600)
level1 = Testlevel()
mygame.add_level(level1)

mygame.run()
print("Ende!")
#x = [tmsge.Animation(), tmsge.Costume(), tmsge.Element(), tmsge.Game(), tmsge.Level(), tmsge.Sprite(), tmsge.Tile(), tmsge.Tileset()]
