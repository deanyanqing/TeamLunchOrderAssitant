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
        #Login(driver)
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
            url = each.get_attribute('href')
            rst_id = each.get_attribute('data-rst-id')
            img = each.find_element_by_class_name('rstblock-logo-icon')
            img_url = img.get_attribute('src')
            
            #default value 
            arrive_time =''
            month_sales = 0
            cost = ''
            promotion = ''

                            
            element_content = each.find_element_by_class_name('rstblock-content')            
            try:
                title = element_content.find_element_by_class_name('rstblock-title').text
                month_sales = element_content.find_element_by_class_name('rstblock-monthsales').text
                cost = element_content.find_element_by_class_name('rstblock-cost').text
                promotion = element_content.find_element_by_class_name('rstblock-activity').text
            except:
                print('Catch excepiton in restaunt',title)
             
            try: 
                arrive_time = each.find_element_by_class_name('rstblock-logo').find_element_by_tag_name('span').text
            except:
                #Don'know arrive time has no meaning,skiping this
                print('Skiping  the unknow arrive time of restaunt', title)
                continue    
            
            #info = each.text
            info = (arrive_time,title,month_sales,cost,promotion)
            restaunt_infos.append((restaunt_id,url,rst_id,img_url,info))
            restaunt_id = restaunt_id + 1
            #print(info)
            #print(img_url,rst_id,url,basic_info)
        driver.close()
        
        #create restaunt with basic info
        self.restaunts =[]
        for info in restaunt_infos:
            self.restaunts.append(Restaurant(info))
    
            
    def refresh_all_restaunt(self):
        for r in self.restaunts:
            r.update_menu()
            r.dump_menu()
    def dump(self):  
        for restaunt in self.restaunts:
            restaunt.dump()
        
