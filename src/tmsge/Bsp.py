class Shape:
    def __init__(self):
        self.x = 10
        self.y = 20

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

class Rect(Shape):
    pass

class Circle(Shape):
    pass

class Figur(Shape):
    def __init__(self):
        super().__init__()
        self.components = []

    def add(self, e):
        self.components.append(e)

    def move(self, dx, dy):
        for e in self.components:
            e.move(dx, dy)

r = Rect()
r.x = 100
r.y = 200
c = Circle()
c.x = 150
c.y = 75

figur = Figur()
figur.add(r)
figur.add(c)

figur.move(5, 10)
print(r)
print(c)