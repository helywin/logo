# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 21:00
# @Author  : Mat
# @Email   : jiang770882022@hotmail.com
# @File    : main.py.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import math


def sinfun(n, k1, k2):
    if n > 0:
        temp = math.pi / 200 * n
        return -math.sin(temp) * math.pow(temp, k1)
    else:
        temp = math.fabs(math.pi / 200 * n)
        return math.sin(temp) * math.pow(temp, k2)

def cosfun(n, k1, k2):
    if n > 0:
        temp = math.pi / 200 * n
        return math.cos(temp) * math.pow(temp, k1)
    else:
        temp = math.fabs(math.pi / 200 * n)
        return -math.cos(temp) * math.pow(temp, k2)


x = []
y = []
k1 = input("输入k1 (1/3.0)>")
k2 = input("输入k2 (1/2.7)>")
w = input("输入线宽 (5)>")
if k1 == '':
    k1 = 1 / 3
else:
    k1 = float(k1)
if k2 == '':
    k2 = 1/2.7
else:
    k2 = float(k2)
if w == '':
    w = '5'

for each in range(-400, 400, 1):
    x.append(cosfun(each, k1, k2))
    y.append(sinfun(each, k1, k2))
fig = plt.plot(x, y, linewidth = w)
plt.axis("equal")
plt.axis('off')
plt.savefig('d:\\logo.png', dpi=300)
plt.show()
# print(x)