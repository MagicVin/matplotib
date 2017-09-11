#!/usr/bin/python3
import matplotlib.pyplot as plt

filename = 'test.txt'
x_value = []
y_value = []
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    x = line.split()[0]
    y = line.split()[1]
    x_value.append(x)
    y_value.append(y)


    #print("x=" + x + "," + "y=" + y)
plt.plot(x_value,y_value,linewidth=1)

#plt.scatter(x_value,y_value,c='red',edgecolors='none',s=100)
#设置图标的主题，并给坐标轴加上标签

plt.title("PTU test", fontsize=24)
plt.xlabel("Temp", fontsize=14)
plt.ylabel("Power",fontsize=14)

#设置刻度标记的大小
#plt.tick_params(axis='both',labelsize=14)

#隐藏坐标轴
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)

plt.show()
