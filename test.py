#!/usr/bin/python3
import matplotlib.pyplot as plt
import time
import datetime
#x_value1 = [33,44,49,61,63,66,67,69,73]
#y_value1 = [79.58,79.59,79.71,80.07,80.1,81.35,81.63,81.8,82.45]
#x_value2 = [35,47,56,62,65,68,70,76,73]
#y_value2 = [80,79,81,80.4,80.6,81.8,81.6,81.5,82]
x_value = []
y_value = []
filename = "tes"
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    x = line.split()[0]
    y = line.split()[1]
    x_value.append(x)
    y_value.append(y)


plt.plot(x_value,y_value,linewidth=1)
#plt.plot(x_value2,y_value2,linewidth=1)
plt.show()
#print(time.time())
#print(time.strftime(ISOTIMEFORMAT,time.localtime()))
#str = str(datetime.datetime.now())
#time = str.split(' ')[0]
#print(time)
