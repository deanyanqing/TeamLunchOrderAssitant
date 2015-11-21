'''
Created on Jun 1, 2015

@author: qiwei
'''

from selenium import webdriver
from selenium import cookie
ELEME_URL = 'https://account.ele.me/login'
USER_NAME = ''
USER_PASSWORD =''
class Login():
    
    def __init__(self, webdriver):
        webdriver.get(ELEME_URL)
        '''
        user_name = webdriver.find_element_by_css_selector('body > div > div > div > div > div:nth-child(2) > form > div:nth-child(2) > input')
        user_name.clear()
        user_name.send_keys(USER_NAME)
        passwd = webdriver.find_element_by_css_selector('body > div > div > div > div > div:nth-child(2) > form > div:nth-child(3) > input')
        passwd.clear()
        passwd.send_keys(USER_PASSWORD)
        '''
        webdriver.manage().add_cookie(cookie())
        