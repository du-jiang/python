import math
class RP(object):
    def __init__(self,n = 3,side = 1,x = 0,y = 0):
        self.n = n
        self.side = n
        self.x = x
        self.y = y
    def Area(self):
        A = (self.n*self.side*self.side)/4*math.tan(math.pi/self.n)
        print(A)
    def perimeter(self):
        P = self.n * self.side
        print(P)

rp = RP()
rp.Area()
rp.perimeter()
print('---------------')
import math
class RP(object):
    def __init__(self,n = 3,side = 1,x = 0,y = 0):
        self.n = n
        self.side = n
        self.x = x
        self.y = y
    def Area(self):
        A = (self.n*self.side*self.side)/4*math.tan(math.pi/self.n)
        print(A)
    def perimeter(self):
        P = self.n * self.side
        print(P)

rp = RP(6,4)
rp.Area()
rp.perimeter()
print('---------------')
import math
class RP(object):
    def __init__(self,n = 3,side = 1,x = 0,y = 0):
        self.n = n
        self.side = n
        self.x = x
        self.y = y
    def Area(self):
        A = (self.n*self.side*self.side)/4*math.tan(math.pi/self.n)
        print(A)
    def perimeter(self):
        P = self.n * self.side
        print(P)

rp = RP(10,4,5.6,7.8)
rp.Area()
rp.perimeter()
        