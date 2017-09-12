#!/usr/bin/python3
import matplotlib.pyplot as plt

filename = 'test.txt'
x_value = []
y_value = []
oddNumX_value = [] #奇数列X值
oddNumY_value = [] #奇数列Y值
evenNumX_value = [] #偶数列X值
evenNumY_value = [] #偶数列Y值

#remainder
i = 0

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    i += 1
    #print("i = " + str(i))
    remainder = i % 2
    #print("remainder = " + str(remainder))
    if remainder == 0: #属于偶数列的数据
        x = line.split()[0]
        y = line.split()[1]
        evenNumX_value.append(x)
        evenNumY_value.append(y)
    elif remainder == 1: #属于奇数列的数据
        x = line.split()[0]
        y = line.split()[1]
        oddNumX_value.append(x)
        oddNumY_value.append(y)
    else :
        print("Sorry , data error!")



#length = len(oddNumX_value) + 1
#遍历列表
#odd_count = 0
#for oddx in oddNumX_value:
#    print("oddx = " + oddx + " oddy = " + oddNumY_value[odd_count])
#    odd_count += 1

#print("count = " + str(count))
#even_count = 0
#for evenx in evenNumX_value:
#    print("evenx = " + evenx + " eveny = " + evenNumY_value[even_count])
#    even_count += 0



#print("length = " + str(length) )
#while i <= length:
#    print("i = " + i)
    #print("odd_x = " + str(oddNumX_value[i]) + "," + "odd_y = " + str(oddNumY_value[i]) )
#    i += 1
    #x_value.append(x)
    #y_value.append(y)


    #print("x=" + x + "," + "y=" + y)
#plt.plot(x_value,y_value,linewidth=1)
plt.plot(evenNumX_value,evenNumY_value,linewidth=2)
#plt.plot(oddNumX_value,oddNumY_value,linewidth=2)
#plt.scatter(x_value,y_value,c='red',edgecolors='none',s=100)
#设置图标的主题，并给坐标轴加上标签

#plt.title("PTU test", fontsize=24)
#plt.xlabel("Temp", fontsize=14)
#plt.ylabel("Power",fontsize=14)

#设置刻度标记的大小
#plt.tick_params(axis='both',labelsize=14)

#隐藏坐标轴
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)

plt.show()
