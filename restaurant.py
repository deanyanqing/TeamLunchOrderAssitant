'''
Created on Jun 2, 2015

@author: qiwei
'''

'''
foods store as dict
 {catalog,[food1:food2]},
 {}


'''
class Restaurant(object):
    '''
    classdocs
    '''


    def __init__(self, name,url):
        '''
        Constructor
        '''
        self.name = name
        self.url = url
        self.foods={}
        self.hot_foods=[]
        self.billboard=''
        
    def addFoods(self,foods,catalog):    
        self.foods[catalog] = foods
        
    def addFood(self,food,catalog):    
        foods = self.foods.get(catalog,[])
        foods.append(food)
        
    def addHotFoods(self,food):
        self.hot_foods    