import tmsge
import pygame
import time

class TestLevel(tmsge.Level):

    def init(self):
        self.background = tmsge.Rectangle(self.game.width, self.game.height, (255, 255, 255))
        self.testsprite = tmsge.Sprite(10, 10, 64, 64)
        self.testsprite2 = tmsge.Sprite(10, 30, 20, 20)
        
        image = tmsge.Spritesheet("ABSOL.png", 64, 64, 4, 4, 10)
        image2 = tmsge.Spritesheet("MORPEKO.png", 64, 64, 4, 4, 10)
        
        self.testsprite.add_costume("test", image)
        self.testsprite2.add_costume("test", image2)
        
        self.testsprite.x = 200
        self.testsprite.y = 300
        self.testsprite2.x = 200
        self.testsprite2.y = 300
        
        self.add_actor(self.testsprite)
        self.add_actor(self.testsprite2)
        
        self.bind(tmsge.EventType.KEYDOWN, self.on_key_down)
        self.bind(tmsge.EventType.KEYUP, self.on_key_up)
        self.bind(tmsge.EventType.KEYDOWN, self.on_key_down2)
        self.bind(tmsge.EventType.KEYUP, self.on_key_up2)
        
        self.testsprite.bind(tmsge.EventType.MOUSEBUTTONDOWN, self.on_sprite_click)
        
        self.testsprite.bind(tmsge.EventType.COLLIDE, self.on_collide)
        
        self.dx = 0
        self.dy = 0
        
        self.dx2 = 0
        self.dy2 = 0
    
    def on_collide(self, event):
        print("COLLIDE!",time.time())
        
    def on_sprite_click(self, event):
        print("SPRITE CLICK")
        
    def on_key_down(self, event):
        if event.key == tmsge.KeyType.LEFT:
            self.dx = -1
            self.testsprite.costume.row = 1
            self.testsprite.costume.running = True
        elif event.key == tmsge.KeyType.RIGHT:
            self.dx = 1
            self.testsprite.costume.row = 2
            self.testsprite.costume.running = True
        elif event.key == tmsge.KeyType.UP:
            self.dy = -1
            self.testsprite.costume.row = 3
            self.testsprite.costume.running = True
        elif event.key == tmsge.KeyType.DOWN:
            self.dy = 1
            self.testsprite.costume.row = 0
            self.testsprite.costume.running = True
    
    def on_key_down2(self, event):
        if event.key == tmsge.KeyType.a:
            self.dx2 = -1
            self.testsprite2.costume.row = 1
            self.testsprite2.costume.running = True
        elif event.key == tmsge.KeyType.d:
            self.dx2 = 1
            self.testsprite2.costume.row = 2
            self.testsprite2.costume.running = True
        elif event.key == tmsge.KeyType.w:
            self.dy2 = -1
            self.testsprite2.costume.row = 3
            self.testsprite2.costume.running = True
        elif event.key == tmsge.KeyType.s:
            self.dy2 = 1
            self.testsprite2.costume.row = 0
            self.testsprite2.costume.running = True
                
    def on_key_up(self, event):
        if event.key == tmsge.KeyType.LEFT or event.key == tmsge.KeyType.RIGHT:
            self.dx = 0
        elif event.key == tmsge.KeyType.UP or event.key == tmsge.KeyType.DOWN:
            self.dy = 0
        self.testsprite.costume.running = False
    
    def on_key_up2(self, event):    
        if event.key == tmsge.KeyType.a or event.key == tmsge.KeyType.d:
            self.dx2 = 0
        elif event.key == tmsge.KeyType.w or event.key == tmsge.KeyType.s:
            self.dy2 = 0
        self.testsprite2.costume.running = False
    
    def act(self):
        
        self.testsprite.x += self.dx
        self.testsprite.y += self.dy
                
        if self.testsprite.x > self.game.width:
            self.testsprite.x = self.game.width
        elif self.testsprite.x < 0:
            self.testsprite.x = 0
        
        if self.testsprite.y > self.game.height:
            self.testsprite.y = self.game.height
        elif self.testsprite.y < 0:
            self.testsprite.y = 0
            
        self.testsprite2.x += self.dx2
        self.testsprite2.y += self.dy2

        if self.testsprite2.x > self.game.width:
            self.testsprite2.x = self.game.width
        elif self.testsprite2.x < 0:
            self.testsprite2.x = 0
        
        if self.testsprite2.y > self.game.height:
            self.testsprite2.y = self.game.height
        elif self.testsprite2.y < 0:
            self.testsprite2.y = 0
        
testgame = tmsge.Game(600, 400)
testlevel = TestLevel()

testgame.add_level(testlevel)
testgame.run()

#x = [tmsge.Animation(), tmsge.Costume(), tmsge.Element(), tmsge.Game(), tmsge.Level(), tmsge.Sprite(), tmsge.Tile(), tmsge.Tileset()]
