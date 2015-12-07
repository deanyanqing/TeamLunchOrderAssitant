'''
Created on Nov 20, 2015

@author: qiwei
'''
import urllib.request
import json
from .login import ElemeLogin
from .login import cookie

URL_CHECKOUT = 'http://www.ele.me/restapi/v1/carts/checkout'
URL_ADDRESET = 'http://www.ele.me/restapi/v1/users/15618394/addresses'

class Order():
    '''
    Response for collect and submit orders
    '''

    def __init__(self,user_id):
        '''
        '''
        HEADER_DICT = {'User-Agent':
                       'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}
        self.url_address = 'http://www.ele.me/restapi/v1/users/' +  str(user_id) +'/addresses'
        
    '''
    
    {"action":"checkout","come_from":"web","geohash":"wtw3s4bd4p4","sig":"75674a7e57f74d33e5989f8e4baa79ee",
    "address_id":44282683,"entities":[
    [{"category_id":1,"name":"秘制黑椒鸡排饭","price":28,"id":45567190,"garnish":[],"specs":[],"quantity":1},
    {"category_id":1,"name":"墨西哥超辣大鸡排","price":14,"id":650748,"garnish":[],"specs":[],"quantity":1}]],"paymethod_id":1}
    '''    
        
    def add_order_shopping_cart(self, orders):
        '''
        @brief Submit orders to Eleme Server 
        @param  orders:  List of dictionary
        Format follow the [{"id":3803277,"quantity":1,"name":"超级大鸡排","price":13,"specs":[]}]
        '''
        values = {"action":"checkout","come_from":"web","geohash":"wtw3s4bd4p4",
                  "entities":[]}
        values['entities'][0] = orders
        values = json.dumps(values)
        url_values = values.encode(encoding='utf-8')
        
        request = urllib.request.Request(method="POST", url=URL_CHECKOUT, data=url_values, headers=self.HEADER_DICT)
        request.add_header('Accept', 'application/json, text/plain, */*')
        response = urllib.request.urlopen(request)
        response = json.loads(response.read().decode('utf-8'))

    def _delivery_addrese(self):
        request = urllib.request.Request(method="GET", url=self.url_address, headers=self.HEADER_DICT)
        request.add_header('Accept', 'application/json, text/plain, */*')
        response = urllib.request.urlopen(request)
        response = urllib.request.urlopen(request)
        response = json.loads(response.read().decode('utf-8'))
        
        for address in response:
            print(address['id'], address['address'])
    
    def query_order(self):
        pass
