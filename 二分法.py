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
n = input("x��n�η� n=")
a = input("����������a=")
b = input("����������b=")
e = input("����e=")
print "�����������������ʽϵ��"
i = 1
while n + 1:
    t.append(input("ϵ��:"))
    n = n - 1

if (fun(t, a) * fun(t, b)) >= 0:
    print "��ֵ�򲻴��ڸ�"
while b - a > e:
    x = 0.5 * (a + b)
    if fun(t, a) * fun(t, x) > 0:
        a = x
    else:
        b = x
print "x��[a,b]�ĸ�Ϊ:"+x

exit = input("Press Enter to exit")
