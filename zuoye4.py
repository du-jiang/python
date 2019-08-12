from prettytable import PrettyTable
x = PrettyTable(["years", "future"])  

x.align["years"] = "l"

x.padding_width = 1
a = input("请输入投资额")
b = input("请输入年利率")
for i in range(1,31):
    f = a+(a*b)*i
    x.add_row([i,f])  