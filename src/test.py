import tmsge

class TestLevel(tmsge.Level):

    def init(self):
        self.background = tmsge.Rectangle(self.game.width, self.game.height, (255, 255, 255))
        self.testsprite = tmsge.Sprite(10, 10, 20, 20)
        image = tmsge.Image("test.png")
        self.testsprite.add_costume("test", image)

        self.add_actor(self.testsprite)

    def act(self):
        if self.testsprite.x > self.game.width:
            self.testsprite.x = 0
        self.testsprite.x += 1
        
testgame = tmsge.Game(600, 400)
testlevel = TestLevel()

testgame.add_level(testlevel)
testgame.run()

#x = [tmsge.Animation(), tmsge.Costume(), tmsge.Element(), tmsge.Game(), tmsge.Level(), tmsge.Sprite(), tmsge.Tile(), tmsge.Tileset()]
