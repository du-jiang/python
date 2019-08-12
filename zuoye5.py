class zuoye(object):
    def printChars(self):
        for i in range(1,27):
            if i % 11 == 0:
                print("\n")
            else:
                print(chr(i+ord('A')),end="")
a=zuoye()
a.printChars()
