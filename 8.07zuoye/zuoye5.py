class eryuan(object):
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
    
    
    def getX(self):
        if self.a*self.d - self.b*self.c != 0:
            x = (self.e*self.d-self.b*self.f) / (self.a*self.d-self.b*self.c)
            print('X为：',x)
        else:
            print('这个方程式无解')
    def getY(self):
        if self.a*self.d - self.b*self.c != 0:
            y = (self.a*self.f-self.e*self.c) / (self.a*self.d-self.b*self.c)
            print('Y为：',y)
        else:
            print('这个方程式无解')
qiujie = eryuan(9,6,4,8,3,5)
qiujie.getX()
qiujie.getY()

