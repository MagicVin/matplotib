#!/usr/bin/python3
#from pygal_maps_world.i18n import COUNTRIES --is good
from pygal.maps.world import COUNTRIES

#print(COUNTRIES)
#for country_code in sorted(COUNTRIES.keys()):
#for country_code in COUNTRIES.keys():
#   print(country_code,COUNTRIES[country_code])COUNTRIES.keys()

def get_country_code(country_name):
    #根据指定的国家，返回Pygal使用的两个字母的国别码
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    #如果没有找到指定的国家，就返回none
    return None
