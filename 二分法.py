# coding=gbk
import math

def fun(list, x):
    max = len(list)
    s = 0
    for i in list:
        s = s + i * (x ** max)
        max = max - 1
    return s

t = []
n = input("x的n次方 n=")
a = input("定义域下限a=")
b = input("定义域上限b=")
e = input("精度e=")
print "下面请依次输入多项式系数"
i = 1
while n + 1:
    t.append(input("系数:"))
    n = n - 1

if (fun(t, a) * fun(t, b)) >= 0:
    print "此值域不存在根"
while b - a > e:
    x = 0.5 * (a + b)
    if fun(t, a) * fun(t, x) > 0:
        a = x
    else:
        b = x
print "x在[a,b]的根为:"+x

exit = input("Press Enter to exit")
