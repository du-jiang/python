class Fan(object):
    def fengshan(self,speed = 1,on = False,radius = 5,color = 'blue'):
        self.speed = speed
        self.on = on
        self.radius = radius
        self.color = color
        print(self.speed,self.on,self.radius,self.color)

fan = Fan()
fan.fengshan(3,True,10,'yellow')


class Fan(object):
    def fengshan(self,speed = 1,on = False,radius = 5,color = 'blue'):
        self.speed = speed
        self.on = on
        self.radius = radius
        self.color = color
        print(self.speed,self.on,self.radius,self.color)

fan = Fan()
fan.fengshan(2,False,5,'blue')