'''
Created on Nov 13, 2015

@author: qiwei
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from check_proxy import has_proxy
from generate_chrome_proxy import generate_chrome_proxy
import os.path
from  restaurant import Restaurant

CSS_OF_SEARCH = '#globalsearch'
CSS_OF_MENU_LIST = 'div.place-rstbox.clearfix > div.clearfix > a ~ a'

class RestauntsManager():

    def __init__(self, location):
        self.update_nearby(location)
    
    def web_driver_no_proxy(self):
        driver = webdriver.Firefox()
        return driver
    def web_driver_with_proxy(self):
        #fix proxy problem 
        #profile = webdriver.FirefoxProfile()
        #profile.set_preference("network.proxy.type", 1);
        #profile.set_preference('network.proxy.http', "114.66.81.130")
        #profile.set_preference("network.proxy.http_port", 8080);
        #driver = webdriver.Firefox(firefox_profile=profile)
    
        pluginfile = 'proxy_auth_plugin.zip'
        if  False == os.path.exists(pluginfile):
            generate_chrome_proxy()
        
        
        co = Options()
        co.add_argument("--start-minimized")
        co.add_extension(pluginfile)
        
        driver = webdriver.Chrome(chrome_options=co)
        return driver
    def web_driver(self):    
        if has_proxy():
            return self.web_driver_with_proxy()
        else:
            return self.web_driver_no_proxy()
        
    #def fix_proxy_cdl(self,driver):
        #driver.send_keys(Keys.TAB)
        #alert = driver.switch_to().alert();
        #alert = driver.switch_to_alert
        #alert.authenticate('','')
        
    def select_restaunt(self,id):  
        pass
      
    def url_of_location(self,loc):
        # Hard code for CDＬ
        return 'http://ele.me/place/wtw3s4bd4p4'
    def update_nearby(self,location):
        url = self.url_of_location(location)
        driver = self.web_driver()
        driver.get(url)
        
        time.sleep(2)
        
        #user cookie to login
        
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
    
restaunt_manager = RestauntsManager('shanghai')        