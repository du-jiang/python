class zuoye(object):
    def getPentagonalNumber(n):
        for i in range(1,101):
            n = i*(3*i-1)/2
            if i % 11 == 0:
                print("\n")
            else:
                print(n,end=" ")
a=zuoye()
a.getPentagonalNumber()