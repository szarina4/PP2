

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length=1):
        Shape.__init__(self)
        self.length = length
    def area(self):
        return self.length**2

a=Square(5)
        