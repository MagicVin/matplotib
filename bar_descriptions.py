#!/usr/bin/python3
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=0, show_legend=False,show_y_guides = False)

chart.title = 'Python Projects'
chart.x_labels = ['awesome-python','httpie','django']
plot_dicts = [
    {'value': 16101, 'label': 'Description of awesome-python.'},
    {'value': 15028, 'label': 'Description of httpie.'},
    {'value': 14798, 'label': 'Description of django.'},
    ]
chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')
