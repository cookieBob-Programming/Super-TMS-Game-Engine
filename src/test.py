import tmsge

class Testlevel(tmsge.Level):
    def __init__(self):
        super().__init__()
        spritesheet = tmsge.Spritesheet("/home/luca/Schreibtisch/Super-TMS-Game-Engine/Game engine/Sprites/Costumes/ABSOL.png", 64, 64, 4, 4, 0, 0)
        animation = tmsge.Animation(spritesheet, 1, 1, 4)
        sprite1 = tmsge.Sprite()
        sprite1.add_costume("animation", animation)
        self.add_element(sprite1)
        animation.tick()
        for event in tmsge.Game.get_events():
            print(event)

mygame = tmsge.Game(800,600)
level1 = Testlevel()
mygame.add_level(level1)
mygame.run()
print("Ende!")
#x = [tmsge.Animation(), tmsge.Costume(), tmsge.Element(), tmsge.Game(), tmsge.Level(), tmsge.Sprite(), tmsge.Tile(), tmsge.Tileset()]
