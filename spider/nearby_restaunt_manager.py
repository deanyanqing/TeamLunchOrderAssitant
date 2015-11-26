'''
Created on Nov 13, 2015

@author: qiwei
'''

from selenium.webdriver.common.keys import Keys
import time

from spider.restaurant import Restaurant
from spider.login import Login
from spider.utility import *

CSS_OF_SEARCH = '#globalsearch'
CSS_OF_MENU_LIST = 'div.place-rstbox.clearfix > div.clearfix > a ~ a'

class RestauntsManager():
    '''
    self.restaunts : list of spider.Restaurant
    
    '''

    def __init__(self, location):
        self.update_nearby(location)

        
    #def fix_proxy_cdl(self,driver):
        #driver.send_keys(Keys.TAB)
        #alert = driver.switch_to().alert();
        #alert = driver.switch_to_alert
        #alert.authenticate('','')
        
    def all_restaunt(self):    
        return self.restaunts
    
    def select_restaunt(self,id):  
        pass
      
    def url_of_location(self,loc):
        # Hard code for CDＬ
        return 'http://ele.me/place/wtw3s4bd4p4'
    def update_nearby(self,location):
        url = self.url_of_location(location)
        driver = web_driver()
        Login(driver)
        driver.get(url)
        
        time.sleep(5)
        
        #Aim to triggle javascript to get more restaunts         
        search = driver.find_element_by_css_selector(CSS_OF_SEARCH)
        search.click()
        for var in range(1,5):                                          
            search.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
        
        
        #from selenium.webdriver import ActionChains
        #action_chains = ActionChains(driver)
        #action_chains.key_down(Keys.PAGE_DOWN).perform()
        
        elem = driver.find_elements_by_css_selector(CSS_OF_MENU_LIST)
        print('Numbers of restuantus=',len(elem))
        
        restaunt_infos =[]
        restaunt_id = 0
        for each in elem:
            info = each.text
            url = each.get_attribute('href')
            rst_id = each.get_attribute('data-rst-id')
            img = each.find_element_by_class_name('rstblock-logo-icon')
            img_url = img.get_attribute('src')
            restaunt_infos.append((restaunt_id,url,rst_id,img_url,info))
            restaunt_id = restaunt_id + 1
            #print(img_url,rst_id,url,basic_info)
        driver.close()
        
        #create restaunt with basic info
        self.restaunts =[]
        for info in restaunt_infos:
            self.restaunts.append(Restaurant(info))
    
    def dump(self):  
        for restaunt in self.restaunts:
            restaunt.dump()
        