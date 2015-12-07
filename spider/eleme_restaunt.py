'''
Created on Nov 27, 2015

@author: qiwei
'''
import urllib.request
import json


URL_ELEME_API = 'http://www.ele.me/restapi/batch'


class ElemeRestaunt():
    '''
    classdocs
    ＠brief Get all eleme restaunt relative information mainly include menu
    '''

    def __init__(self, restaurant_id):
        '''
        Maintain all detail menus of restaunt
        @param restaurant_id
        '''
        self.id = restaurant_id
        self.menu = { }

    def load_menu(self):
        # No Host and Referere here ,otherwise rejected with errorcode=400
        header_dict = {'User-Agent':
                       'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}

        values = {"timeout":10000,"requests":[{"method":"GET","url":"/v4/restaurants/" + self.id+"/mutimenu"}
                                              # {"method":"GET","url":"/v1/users/favor/restaurants/"+ self.id}
                                              ]}
        datas = json.dumps(values)

        url_values = datas.encode(encoding='utf-8')
        request = urllib.request.Request(method="POST", url=URL_ELEME_API, data=url_values, headers=header_dict)
        request.add_header('Accept', 'application/json, text/plain, */*')
        # request.add_header('Content-Length', '147')

        response = urllib.request.urlopen(request)
        response = json.loads(response.readall().decode('utf-8'))
        # print(response)
        menus = self._parse_http_response(response)
        return menus
    
    # Highly dependency with http request 
    def _parse_http_response(self, response_json):
        #print(response_json)
        menu_json = response_json[0]['body']
        print(len(menu_json))
        for menu in menu_json:
            print(menu['name'])

    def refreseh_menu(self):
        pass