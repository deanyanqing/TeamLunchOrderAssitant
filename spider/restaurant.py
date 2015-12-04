'''
Created on Jun 2, 2015

@author: qiwei
'''
from spider.html_handler import HtmlHandler
import os
import re


class Restaurant():
    '''
    classdocs
    Out of date since there is no JSON embed in HTML
    Need to invoke update_menu to get the detail menu
    '''
    dataSrcDir = os.path.join(os.environ['HOME'], 'lunchRes', 'image')
    if not os.path.exists(dataSrcDir):
        os.makedirs(os.path.join(os.environ['HOME'], dataSrcDir))

    exatc_re = re.compile('([^\n]+)\n([^\n]+)\n([^\n]+)\n([^\n]+)\n([^\n]+)')

    def __init__(self, basic_info):
        (_, self.url, self.rst_id, self.img_url, info) = basic_info
        # print(info)
        (self.arrive_time, self.name, self.sales, self.delivery_limit, self.promotion) = info
        self.foods = {}
        self.hot_foods = []
        self.billboard = ''

    def dump(self):
        print(self.url, self.rst_id, self.img_url, self.arrive_time, self.name, self.sales, self.delivery_limit, self.promotion)

    def dump_menu(self):
        for c in self.catalogues:
            c.dump()

    def update_menu(self):
        handler = HtmlHandler(self.url)
        self.catalogues = handler.phaseHtml()
        (self.logo, self.name, self.raking) = handler.getBasicRestauntInfo()

    def setBasicInfo(self):
        print("Basic info")

    def addFoods(self, foods, catalog):
        self.foods[catalog] = foods

    def addFood(self, food, catalog):
        foods = self.foods.get(catalog, [])
        foods.append(food)

    def addHotFoods(self, food):
        self.hot_foods
# restaunt= Restaurant("http://r.ele.me/dml96518")
# restaunt= Restaurant("http://r.ele.me/lzx-775")
