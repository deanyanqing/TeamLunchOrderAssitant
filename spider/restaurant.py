'''
Created on Jun 2, 2015

@author: qiwei
'''
from HtmlHandler import HtmlHandler 
import os
'''

'''
class Restaurant():
    '''
    classdocs
    '''
    dataSrcDir=os.path.join(os.environ['HOME'],'lunchRes','image')
    if not os.path.exists(dataSrcDir):
        os.makedirs(os.path.join(os.environ['HOME'],dataSrcDir)) 

    def __init__(self, url):
        '''
        Constructor
        '''
        self.url = url
        self.foods={}
        self.hot_foods=[]
        self.billboard=''
        handler=HtmlHandler(url)
        #self.catalogues=handler.phaseHtml()
        (self.logo,self.name,self.raking) = handler.getBasicRestauntInfo()
        
    def addFoods(self,foods,catalog):    
        self.foods[catalog] = foods
        
    def addFood(self,food,catalog):    
        foods = self.foods.get(catalog,[])
        foods.append(food)
        
    def addHotFoods(self,food):
        self.hot_foods   
restaunt= Restaurant("http://r.ele.me/dml96518")
#restaunt= Restaurant("http://r.ele.me/lzx-775")