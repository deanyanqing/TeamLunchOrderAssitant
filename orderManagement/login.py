'''
Created on Dec 8, 2015

@author: qiwei
'''
import urllib.request
import json
import copy

class ElemeLogin():
    '''
    Step 1: Involke image_of_verificaiton to get verification image_of_verificaiton
    Step 2: Login with username,passwd,code
    '''
    URL_LOGIN = 'https://account.ele.me/login'

    def __init__(self):
        header_dict = {'User-Agent':
                       'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}

    def image_of_verificaiton(self):

        pass
        
    def login(self, user, password, verificaion_code):
        pass
