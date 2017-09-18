#!/usr/bin/python3
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as LS

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']
print("Number of items:",len(repo_dicts))

#研究第一个仓库
#repo_dict = repo_dicts[0]
#for repo_dict in repo_dicts:
#    print("\nSelected information about first repository:")
#    print('Name:',repo_dict['name'])
#    print('Owner:',repo_dict['owner']['login'])
#    print('Stars:',repo_dict['stargazers_count'])
#    print('Repository:',repo_dict['html_url'])
#    print('Created:',repo_dict['created_at'])
#    print('Updated:',repo_dict['updated_at'])
#    print('Description:',repo_dict['description'])

stars, names, plot_dicts = [], [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    plot_dict = {
    'value':repo_dict['stargazers_count'],
    'label':str(repo_dict['description']),
    }
    plot_dicts.append(plot_dict)



#可视化
my_style = LS('#333366',base_style=LCS)
#创建Pygal类Config的实例
my_config = pygal.Config()
#设置X轴X坐标的旋转角度
my_config.x_label_rotation = -45
#隐藏图例
my_config.show_legend = False
#设置图标标题的字体大小
my_config.title_font_size = 24
#设置副标签的字体大小
#副标签是x轴上的项目名以及y轴上的大部分数字
my_config.label_font_size = 14
#设置住标签的字体大小
#主标签是y轴上为5000整数倍的刻度;这些标签应更大,以与副标签区分开来
my_config.major_label_font_size = 20
#设置项目名称为15个字符
my_config.truncate_label = 25
#隐藏图表中的水平线
my_config.show_y_guides = False
#设置地定义宽度
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)

#LS:设置基色 #333366
#x_label_rotation：设置旋转角度
#show_legend=False:隐藏图例
#chart.x_labels:显示横坐标值

chart.title = 'Most-Starred python Projects on GitHub'
    #'':显示备注标签
    #stars:纵坐标值
#chart = pygal.Bar(style=my_style,x_label_rotation=-45,show_legend=False)
chart.x_labels = names
#chart.add('',stars)
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
