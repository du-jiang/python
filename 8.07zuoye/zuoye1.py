class Rectangle(object):
    def __init__(self,width = 1,height = 2):
        self.width=width
        self.height=height
        print(self.width)
        print(self.height)
    def getArea(self):
        area = self.height * self.width
        print(area)
    def getPerimeter(self):
        zhouchang = self.height * 2 + self.width * 2
        print(zhouchang)
juxing = Rectangle()   
juxing.getArea()
juxing.getPerimeter()
print('--------------')
class Rectangle(object):
    def __init__(self,width = 1,height = 2):
        self.width=width
        self.height=height
        print(self.width)
        print(self.height)
    def getArea(self):
        area = self.height * self.width
        print(area)
    def getPerimeter(self):
        zhouchang = self.height * 2 + self.width * 2
        print(zhouchang)
juxing = Rectangle(4,40)   
juxing.getArea()
juxing.getPerimeter()

print('--------------')
class Rectangle(object):
    def __init__(self,width = 1,height = 2):
        self.width=width
        self.height=height
        print(self.width)
        print(self.height)
    def getArea(self):
        area = self.height * self.width
        print(area)
    def getPerimeter(self):
        zhouchang = self.height * 2 + self.width * 2
        print(zhouchang)
juxing = Rectangle(3.5,35.7)   
juxing.getArea()
juxing.getPerimeter()