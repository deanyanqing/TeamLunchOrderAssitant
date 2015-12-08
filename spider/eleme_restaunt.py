'''
Created on Nov 27, 2015

@author: qiwei
'''
import urllib.request
import json
import copy

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
        # name is group name, all detail menu store in foods
        self.group = {'name': '', 'foods': []}
        self.foods_key = ['rating', 'tips', 'month_sales', 'restaurant_id', 'name', 'image_path', 'rating_count', 'limitation', 'specfoods']
        self.specfoods = ['food_id', 'packing_fee', 'price', 'name']

    def load_menu(self):
        # No Host and Referere here ,otherwise rejected with errorcode=400
        header_dict = {'User-Agent':
                       'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}

        values = {"timeout": 10000, "requests": [{"method": "GET", "url": "/v4/restaurants/" + self.id+"/mutimenu"}
                                                 # {"method":"GET","url":"/v1/users/favor/restaurants/"+ self.id}
                                                 ]}
        datas = json.dumps(values)

        url_values = datas.encode(encoding='utf-8')
        request = urllib.request.Request(method="POST", url=URL_ELEME_API, data=url_values, headers=header_dict)
        request.add_header('Accept', 'application/json, text/plain, */*')
        # request.add_header('Content-Length', '147')

        response = urllib.request.urlopen(request)
        response = json.loads(response.read().decode('utf-8'))
        # print(response)
        menus = self._parse_http_response(response)
        return menus

    # Highly dependency with http request
    def _parse_http_response(self, response_json):

        menu_json = response_json[0]['body']
        menu_json = json.loads(menu_json)
        print(len(menu_json))
        menus = []
        for menu in menu_json:
            group = self._parse_group(menu)
            menus.append(group)
        return menus

    def _parse_group(self, group_json):
        group = copy.deepcopy(self.group)
        group['name'] = group_json['name']
        # print(len(group_json['foods']))

        for food in group_json['foods']:
            # print(food['name'])
            my_food = {}
            my_food['specfoods'] = []

            for k in self.foods_key:
                my_food[k] = food[k]
            '''
            for spec_food in food['specfoods']:
                my_sepc_food = {}
                for sepc_k in self.specfoods:
                    my_sepc_food[sepc_k] = spec_food[sepc_k]
                my_food['specfoods'].append(my_sepc_food)
            '''
            group['foods'].append(my_food)

        # print(group)
        return group

    def refreseh_menu(self):
        pass
