#!/usr/bin/python3
#原文：
#from pygal.i18n import COUNTRIES
#pygal.i18n 已被改名：pygal_maps_world
#pygal_maps_world 需要额外安装:
                #root# pip -V
                #pip 9.0.1 from /usr/local/lib/python3.5/dist-packages (python 3.5) --版本
                #sudo su
                #pip install pygal_maps_world

#from pygal_maps_world.i18n import COUNTRIES --is good
from pygal.maps.world import COUNTRIES
#print(COUNTRIES)
for country_code in sorted(COUNTRIES.keys()):
#for country_code in COUNTRIES.keys():
   print(country_code,COUNTRIES[country_code])
