
num1 = input('输入1个整数')
num2 = input('输入1个整数')
num3 = input('输入1个整数')
if num1<num2<num3:
    print(num1,num2,num3)
elif num1<num3<num2:
    print(num1,num3,num2)
elif num2<num3<num1:
    print(num2,num3,num1)
elif num2<num1<num3:
    print(num2,num1,num3)
elif num3<num1<num2:
    print(num3,num1,num2)
elif num3<num2<num1:
    print(num3,num2,num1)
else:
    print("请输入三个不同的整数") 
