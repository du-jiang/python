import numpy as np
from numpy.linalg import solve
class JD(object):
    def __init__(self,x1,x2,x3,x4,y1,y2,y3,y4):
        self.x1=x1
        self.x2=x2
        self.x3=x3
        self.x4=x4
        self.y1=y1
        self.y2=y2
        self.y3=y3
        self.y4=y4
    def JDd(self):
        k1 = (self.x1-self.x2) / (self.y1-self.y2)
        k2 = (self.x3-self.x4) / (self.y3-self.y4)
        if k1 == k2:
            print('两条线段平行，请重新输入坐标')
        else:
            a=np.mat([[self.y1-self.y2,self.x2-self.x1],[self.y3-self.y4,self.x4-self.x3]])#系数矩阵
            b=np.mat([self.y1*self.x2-self.x1*self.y2,self.y3*self.x4-self.x3*self.y4]).T    #常数项列矩阵
            x=solve(a,b)        #方程组的解
            if a*(self.y1-self.y2)+b*(self.x2-self.x1) == self.y1*self.x2-self.x1*self.y2 and a*(self.y3-self.y4)+b*(self.x4-self.x3) == self.y3*self.x4-self.x3*self.y4:
                print(a,b)
            else:
                print('两条线段无交点')
jd = JD(1,2,3,4,5,6,7,8)
jd.JDd()

