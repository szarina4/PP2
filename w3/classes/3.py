class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length=1,width=1):
        Shape.__init__(self)
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

b=Rectangle(2,3)
        