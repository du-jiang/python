class zuoye(object):
    def sumDigits(n):
        num = input('请输入整数：')
        sum = 0
        if num.isdigit():
            for i in range(len(num)):
                cut_num = num[i:i + 1]
                sum = sum + int(cut_num)
                print(sum)
        else:
            print("重新输入")

a=zuoye()
a.sumDigits()
