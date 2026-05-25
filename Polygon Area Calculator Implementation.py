class square:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("Hi,My name is square.My area is :", self.side**2)
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(" Hi,My name is circle. My area is :", 3.14*self.radius*self.radius)
asquare = square(10)
acircle = circle(10)
for shape in (asquare, acircle):
    shape.area()
class square:
    def __init__(self):
        # private attribute
        self.__side = 6
    def area(self):
        print("Hi,I am square,my side is :", self.__side)
        print("Hi,My name is square,My area is :", self.__side**2)
ob = square()
ob.__side = 24
ob.area()