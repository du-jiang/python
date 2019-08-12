class zuoye(object):
    def day(years):
        for i in range(2010,2021):
            if ((i % 4 == 0 and i % 100 != 0) | (i % 400 == 0)):
                print(366)
            else:
                print(365)
a=zuoye()
a.day()