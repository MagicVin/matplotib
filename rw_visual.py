#!/usr/bin/python3
import matplotlib.pyplot as plt
from random_walk import RandoWalk


while True:
    #创建一个RandoWalk实例，并将其包含的点都绘制出来
    rw = RandoWalk()
    rw.fill_walk()

    #设置绘图窗口的尺寸
    plt.figure(dpi=180,figsize=(10,6))
    #绘制点并将图形显示出来
    point_numbers = list(range(rw.num_points))
    #plt.axis([0,5000,0,5000])
    plt.scatter(rw.x_values,rw.y_values,s=15,c=rw.y_values,cmap=plt.cm.Set1,edgecolors="none")
    #plt.scatter(rw.x_values,rw.y_values,s=1,c=point_numbers,cmap=plt.cm.Reds,edgecolors="none")
    #plt.plot(rw.x_values,rw.y_values,linewidth=1)
    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
