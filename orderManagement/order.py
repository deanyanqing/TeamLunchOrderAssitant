'''
Created on Nov 20, 2015

@author: qiwei
'''
import urllib.request
import json

URL_CHECKOUT = 'http://www.ele.me/restapi/v1/carts/checkout'


class Order():
    '''
    Response for collect and submit orders
    '''

    def __init__(self):
        '''
        '''
        HEADER_DICT = {'User-Agent':
                       'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}

    def add_order_shopping_cart(self, orders):
        pass

    def query_order(self):
        pass
