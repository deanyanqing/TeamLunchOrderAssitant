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
        # No Host and Referere here ,otherwise rejected with errorcode=400
        header_dict = {'User-Agent':
                       'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}

        values = {"timeout":10000,"requests":[{"method":"GET","url":"/v4/restaurants/" + restaurant_id+"/mutimenu"}, {"method":"GET","url":"/v1/users/favor/restaurants/"+ restaurant_id}]}
        datas = json.dumps(values)

        url_values = datas.encode(encoding='utf-8')
        request = urllib.request.Request(method="POST", url=URL_ELEME_API, data=url_values, headers=header_dict)
        request.add_header('Accept', 'application/json, text/plain, */*')
        # request.add_header('Content-Length', '147')

        response = urllib.request.urlopen(request)
        response = json.loads(response.readall().decode('utf-8'))
        # print(response)
        self._parse_http_response(response)

        def _parse_http_response(self, response_json):
            pass
