#!/usr/bin/python3
from die import Die
import pygal

#创建一个D6
die1 = Die()
die2 = Die(10)
#掷几次骰子，并将结果存储在一个列表中
results = []

for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    #frequencies.append(value)
    frequencies.append(frequency)

#print (frequencies)

#对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(2,17))
hist.y_title = "Result"
hist.x_title = "frequency of Result"

hist.add('D6 + D10',frequencies)
hist.render_to_file('die_visual.svg')
