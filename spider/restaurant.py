'''
Created on Jun 2, 2015

@author: qiwei
'''
from html_handler import HtmlHandler 
import os
import re
'''

'''
class Restaurant():
    '''
    classdocs
    '''
    dataSrcDir=os.path.join(os.environ['HOME'],'lunchRes','image')
    if not os.path.exists(dataSrcDir):
        os.makedirs(os.path.join(os.environ['HOME'],dataSrcDir)) 

    exatc_re = re.compile('([^\n]+)\n([^\n]+)\n([^\n]+)\n([^\n]+)\n([^\n]+)')
    
    def __init__(self, basic_info):
        (_,self.url , self.rst_id,self.img_url, info) = basic_info
        (self.arrive_time,self.name,self.sales,self.delivery_limit,self.discount ) = self.exatc_re.search(info).group(1,2,3,4,5)
        self.foods={}
        self.hot_foods=[]
        self.billboard=''

    
    def update_menu(self):
        handler=HtmlHandler(self.url)
        self.catalogues=handler.phaseHtml()
        (self.logo,self.name,self.raking) = handler.getBasicRestauntInfo()
    def setBasicInfo(self):  
        print("Basic info")  
        
    def addFoods(self,foods,catalog):    
        self.foods[catalog] = foods
        
    def addFood(self,food,catalog):    
        foods = self.foods.get(catalog,[])
        foods.append(food)
        
    def addHotFoods(self,food):
        self.hot_foods   
#restaunt= Restaurant("http://r.ele.me/dml96518")
#restaunt= Restaurant("http://r.ele.me/lzx-775")