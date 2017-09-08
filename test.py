#!/usr/bin/python3
import matplotlib.pyplot as plt
import time
import datetime
#x_value = [33,44,49,61,63,66,67,69,73]
#y_value = [79.58,79.59,79.71,80.07,80.1,81.35,81.63,81.8,82.45]
#plt.plot(x_value,y_value,linewidth=1)
#plt.show()
#print(time.time())
#print(time.strftime(ISOTIMEFORMAT,time.localtime()))
str = str(datetime.datetime.now())
time = str.split(' ')[0]
print(time)
