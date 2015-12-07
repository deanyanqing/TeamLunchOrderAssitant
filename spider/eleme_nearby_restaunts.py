'''
Created on Dec 5, 2015

@author: qiwei
'''
import urllib.request
import json

URL_OF_CDL_NEARBY = ''''''
URL_ELEME_API = 'http://www.ele.me/restapi/batch'
GEOHASH_OF_CDL = 'wtw3s4bd4p4'

class ElemeNearbyRestauntManager():
    '''
    Maintain  restaunts inforamtion nearby  specify location
    '''


    def __init__(self, location):
        '''
        @param location: Specify geometry locaiton where to delivery the order
        '''
        # No Host and Referere here ,otherwise rejected with errorcode=400
        header_dict = {'User-Agent':\
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}
        geohash = self._geohash(location)
        
        '''
        request 1:Get all fast food : restaurant_category_id=207
        request 2:Get all so called "lunch" : restaurant_category_id=220
        request 3:
        request 4: Get classfication of kinds shops
        No use 5 and 6
        '''
        values = {"timeout":10000,"requests":[
                                              {"method":"GET","url":"/v3/restaurants?extras%5B%5D=food_activity&extras%5B%5D=restaurant_activity&extras%5B%5D=certification&fields%5B%5D=id&fields%5B%5D=name&fields%5B%5D=phone&fields%5B%5D=promotion_info&fields%5B%5D=name_for_url&fields%5B%5D=flavors&fields%5B%5D=is_time_ensure&fields%5B%5D=is_premium&fields%5B%5D=image_path&fields%5B%5D=rating&fields%5B%5D=is_free_delivery&fields%5B%5D=minimum_order_amount&fields%5B%5D=order_lead_time&fields%5B%5D=is_support_invoice&fields%5B%5D=is_new&fields%5B%5D=is_third_party_delivery&fields%5B%5D=is_in_book_time&fields%5B%5D=rating_count&fields%5B%5D=address&fields%5B%5D=month_sales&fields%5B%5D=delivery_fee&fields%5B%5D=minimum_free_delivery_amount&fields%5B%5D=minimum_order_description&fields%5B%5D=minimum_invoice_amount&fields%5B%5D=opening_hours&fields%5B%5D=is_online_payment&fields%5B%5D=status&fields%5B%5D=supports&fields%5B%5D=in_delivery_area&fields%5B%5D=delivery_mode&fields%5B%5D=recent_order_num&geohash=" +geohash+"&limit=24&offset=0&restaurant_category_id=207&type=geohash"},
                                              {"method":"GET","url":"/v3/restaurants?extras%5B%5D=food_activity&extras%5B%5D=restaurant_activity&extras%5B%5D=certification&fields%5B%5D=id&fields%5B%5D=name&fields%5B%5D=phone&fields%5B%5D=promotion_info&fields%5B%5D=name_for_url&fields%5B%5D=flavors&fields%5B%5D=is_time_ensure&fields%5B%5D=is_premium&fields%5B%5D=image_path&fields%5B%5D=rating&fields%5B%5D=is_free_delivery&fields%5B%5D=minimum_order_amount&fields%5B%5D=order_lead_time&fields%5B%5D=is_support_invoice&fields%5B%5D=is_new&fields%5B%5D=is_third_party_delivery&fields%5B%5D=is_in_book_time&fields%5B%5D=rating_count&fields%5B%5D=address&fields%5B%5D=month_sales&fields%5B%5D=delivery_fee&fields%5B%5D=minimum_free_delivery_amount&fields%5B%5D=minimum_order_description&fields%5B%5D=minimum_invoice_amount&fields%5B%5D=opening_hours&fields%5B%5D=is_online_payment&fields%5B%5D=status&fields%5B%5D=supports&fields%5B%5D=in_delivery_area&fields%5B%5D=delivery_mode&fields%5B%5D=recent_order_num&geohash=" +geohash+"&limit=24&offset=0&restaurant_category_id=220&type=geohash"},
                                              {"method":"GET","url":"/v1/content?consumer=3&geohash="+geohash},
                                              {"method":"GET","url":"/v1/restaurant_categories?geohash="+geohash},
                                              {"method":"GET","url":"/v1/user?extras%5B%5D=premium_vip&extras%5B%5D=is_auto_generated"},
                                              {"method":"GET","url":"/v1/users/15618394/places?extras%5B%5D=geohash"}
                                              ]
                  }
        url_values = json.dumps(values).encode(encoding='utf-8')
        request = urllib.request.Request(method="POST", url=URL_ELEME_API, data = url_values, headers=header_dict)
        request.add_header('Accept','application/json, text/plain, */*')
        
        response = urllib.request.urlopen(request)

        response = json.loads(response.readall().decode('utf-8'))
        self._parse_http_response(response)
        # print(the_page.decode("utf8"))
        
    def _parse_http_response(self,response):    
        # Highly dependency with http requests order and content
        fastfoods = self._parse_fast_food(response[0])
        lunches  = self._parse_lunch(response[1])
        catelogs = self._parse_catalogs(response[2])
    
    def _parse_fast_food(self,json_fastfoods):
        pass
    
    def _parse_lunch(self,json_lunch):
        pass
    
    def _parse_catalogs(self,json_result):
        pass
    
    # Hard code for cdl currently    
    def _geohash(self,location):    
        return GEOHASH_OF_CDL
    
    
    def restuants(self):
        '''
        Get all restaunts with basic informaiton NOT include detail menu
        '''
        pass
    
neayRestuantsMgr = ElemeNearbyRestauntManager("")    