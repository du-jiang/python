
class number(object):
    def __init__(self):
        pass
    def a(self,x):
        self.x=x
    def num(self):
        if (self.x%1==0):
            for i in range(2,self.x):
                if(self.x%i == 0):
                    print('不为素数')
                    break
                else:
                    print('是素数')
        else:
            print('请输入正整数')

n=number()
n.a(3.3)
n.num()
        