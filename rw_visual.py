#!/usr/bin/python3
import matplotlib.pyplot as plt
from random_walk import RandoWalk


while True:
    #创建一个RandoWalk实例，并将其包含的点都绘制出来
    rw = RandoWalk()
    rw.fill_walk()
    #plt.axis([0,5000,0,5000])
    plt.scatter(rw.x_values,rw.y_values,s=15,c=rw.y_values,cmap=plt.cm.Set1,edgecolors="none")
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
