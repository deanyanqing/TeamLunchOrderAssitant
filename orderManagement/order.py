'''
Created on Nov 20, 2015

@author: qiwei
'''
import urllib.request
import json
from . login import ElemeLogin
from . login import cookie

URL_CHECKOUT = 'http://www.ele.me/restapi/v1/carts/checkout'

class Order():
    '''
    Response for collect and submit orders
    '''

    def __init__(self, user_id):
        '''
        '''
        self.HEADER_DICT = {'User-Agent':
                            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}
        self.url_address = 'http://www.ele.me/restapi/v1/users/' + str(user_id) + '/addresses'
        self.user_id = user_id
    '''
    {"action":"checkout","come_from":"web","geohash":"wtw3s4bd4p4","sig":"75674a7e57f74d33e5989f8e4baa79ee",
    "address_id":44282683,"entities":[
    [{"category_id":1,"name":"秘制黑椒鸡排饭","price":28,"id":45567190,"garnish":[],"specs":[],"quantity":1},
    {"category_id":1,"name":"墨西哥超辣大鸡排","price":14,"id":650748,"garnish":[],"specs":[],"quantity":1}]],"paymethod_id":1}
    '''

    def submit_orders(self, orders):
        '''
        @brief Submit orders to supplier
        @param  orders:  List of dictionary
        Format follow the [{"id":3803277,"quantity":1,"name":"超级大鸡排","price":13,"specs":[]}]
        @return {}
        '''
        self._checkout_cart(orders)
        result = self._submit_orders()

    def verify_sms_verification(self, code):
        '''
        @brief Verify the SMS verification code
        Whenever submit_orders return need_verification need revolke this method
        @param code : SMS verification code
        '''
        pass

    def _checkout_cart(self, orders):
        '''
        @brief Checkouts orders to Eleme Server

        '''
        values = {"action": "checkout", "come_from": "web", "geohash": "wtw3s4bd4p4",
                  "entities": []}
        values['entities'][0] = orders
        values = json.dumps(values)
        url_values = values.encode(encoding='utf-8')

        # Nothing but follow request sequence of web client in order to triggle HTML download
        request = urllib.request.Request(method="GET", url=URL_CHECKOUT, headers=self.HEADER_DICT)
        request.add_header('Accept', 'application/json, text/plain, */*')
        response = urllib.request.urlopen(request)

        values = {"action": "checkout", "come_from": "web", "geohash": "wtw3s4bd4p4",
                  "entities": []}
        values['entities'][0] = orders
        values = json.dumps(values)
        url_values = values.encode(encoding='utf-8')
        request = urllib.request.Request(method="POST", url=URL_CHECKOUT, data=url_values, headers=self.HEADER_DICT)
        request.add_header('Accept', 'application/json, text/plain, */*')
        response = urllib.request.urlopen(request)
        response = json.loads(response.read().decode('utf-8'))

        self.cart_id = response['cart']['id']
        self.sig_id = response['cart']['sig']

    def _delivery_addrese(self):
        '''
        Retrieve the address_id
        '''
        request = urllib.request.Request(method="GET", url=self.url_address, headers=self.HEADER_DICT)
        request.add_header('Accept', 'application/json, text/plain, */*')
        response = urllib.request.urlopen(request)
        response = urllib.request.urlopen(request)
        response = json.loads(response.read().decode('utf-8'))

        for address in response:
            print(address['id'], address['address'])
            if -1 != str(address['address']).index('宝马'):
                # self.address_id = address['id']
                return address['id']
        # default addresss or throw exception?
        return response[0]['id']

    def _submit_orders(self):
        '''
        cardId = id in response of checkout
        sigID = sig in response of checkout
        '''
        address_id = self._delivery_addrese()
        values = {"userId": 15618394, "cartId": "7faadf50a2e911e58422a4dcbe0b550c", "come_from": "web",
                  "sig": "8070a44b7f2a664e1c2753ccab44ccbc", " ": 1, "description": "",
                  "deliver_time": "12:00", "invoice": "", "bind_mobile": 0, "address_id": 31011502}
        values['userId'] = int(self.user_id)
        values['sig'] = self.sig_id
        values['cartId'] = self.cart_id
        values['address_id'] = int(address_id)

        url_submit_order = 'http://www.ele.me/restapi/v1/users/‘ + str(self.user_id) + ’/carts/' + self.cart_id + '/orders'
        print('Try to submit order to url:' + url_submit_order)
        values = json.dumps(values)
        url_values = values.encode(encoding='utf-8')
        request = urllib.request.Request(method="POST", url=url_submit_order, data=url_values, headers=self.HEADER_DICT)
        request.add_header('Accept', 'application/json, text/plain, */*')

        response = urllib.request.urlopen(request)
        response = json.loads(response.read().decode('utf-8'))
        check_result = self.__check_whether_sms_validation(response)
        if False == check_result['need_validation']:
            pass

    def _check_whether_sms_validation(self, response):
        need_validation = response['need_validation']
        validation_type = response['validation_type']
        return {'need_validation': need_validation, 'validation_type': validation_type}

    def _verfify(self):
        values = {"action": "verify_code", "cartId": "7faadf50a2e911e58422a4dcbe0b550c", "sig": "8070a44b7f2a664e1c2753ccab44ccbc", "type": "sms"}
        values['sig'] = self.sig_id
        values['cartId'] = self.cart_id

        url_verify = 'http://www.ele.me/restapi/v1/carts/' + self.cart_id + '/verify_code'
        values = json.dumps(values)
        url_values = values.encode(encoding='utf-8')
        request = urllib.request.Request(method="POST", url=url_verify, data=url_values, headers=self.HEADER_DICT)
        request.add_header('Accept', 'application/json, text/plain, */*')

        response = urllib.request.urlopen(request)
        response = json.loads(response.read().decode('utf-8'))
        validate_token = response['validate_token']
        print(validate_token)
        
    def _query_order(self):
        pass
