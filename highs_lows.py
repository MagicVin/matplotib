#!/usr/bin/python3
import csv
from matplotlib import pyplot as plt
from datetime import datetime

#filename = 'sitka_weather_07-2014.csv'
filename1 = 'sitka_weather_2014.csv'
filename2 = 'death_valley_2014.csv'
str1 = "Daily high and low temperatures - 2014"
str2 = "Daily high and low temperatures - 2014\nDeath Valley,CA"
dates,highs,lows,test_list = [],[], [], []

def draw(filename1,filename2,string):
    with open(filename1) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            try:

                current_date = datetime.strptime(row[0],"%Y-%m-%d")
                f1_date = "1." + str(current_date).split("-")[1].split()[0]
                #print("f1_date = " ,f1_date)

                high = int(row[1])
                low = int(row[3])

            except ValueError:
                print(current_date,'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
                test_list.append(f1_date)
                #print("f2_date = " ,f2_date)

#    with open(filename2) as n:
#        reader = csv.reader(n)
#        header_row = next(reader)

#        for row in reader:
#            try:
#                current_date = datetime.strptime(row[0],"%Y-%m-%d")
                #f2_date = "f2." + str(current_date)[:7]
#                f2_date = "2." + str(current_date).split("-")[1].split()[0]
#                high = int(row[1])
#                low = int(row[3])
#            except ValueError:
#                print(current_date,'missing data')
#            else:
#                dates.append(current_date)
#                highs.append(high)
#                lows.append(low)
#                test_list.append(f2_date)




    #根据数据绘制图形
    fig = plt.figure(dpi=128,figsize=(10,6))
    #for date in dates:
    #    print("dates = " + str(date))
    format_list = []
    format_list = list(set(test_list))
    #print("test_list = ",test_list)
    #print("format_list = ",format_list)
    format_list.sort(key=test_list.index)
    #print("format_list.sort = ",format_list)

    plt.plot(dates,highs,c='red')
    plt.plot(dates,lows,c='blue')
    #plt.plot(format_list,lows,c='blue')
    #填充温差颜色
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    fig.autofmt_xdate()
    plt.xlabel('',fontsize=16)
    plt.ylabel("Temperatures(F)",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)
    #设置图形的格式
    plt.title( string ,fontsize=24)

draw(filename1,filename2,str1)



plt.show()
