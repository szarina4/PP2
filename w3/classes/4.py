from cmath import sqrt


class Point:
    def __init__(self,x=1,y=1):
        self.x=x
        self.y=y
    def show(self):
        print(f"The x coordinate is {self.x} and y coordinate is {self.y}")
    def move(self,x1=1,y1=1):
        self.x=x1
        self.y=y1
    def dis(self,x1=1,y1=1):
        print(((x1-self.x)**2+(y1-self.y)**2)**0.5)

a=Point(1,4)
a.show()
a.move(0,0)
a.dis(3,2)
