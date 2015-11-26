'''
Created on Jun 1, 2015

@author: qiwei
'''

import time

ELEME_URL = 'https://account.ele.me/login'
USER_NAME = '18616821819'
USER_PASSWORD ='0503andy'
class Login():
    
    def __init__(self, webdriver):
        webdriver.get(ELEME_URL)
        
        user_name = webdriver.find_element_by_css_selector('body > div > div > div > div > div:nth-child(2) > form > div:nth-child(2) > input')
        user_name.clear()
        user_name.send_keys(USER_NAME)
        passwd = webdriver.find_element_by_css_selector('body > div > div > div > div > div:nth-child(2) > form > div:nth-child(3) > input')
        passwd.clear()
        passwd.send_keys(USER_PASSWORD)
        
        time.sleep(10)
        
        #ok = webdriver.find_element_by_css_selector('body > div > div > div > div > div:nth-child(2) > form > div:nth-child(6) > button')
        #ok.click()
        #webdriver.manage().add_cookie(cookie())
        