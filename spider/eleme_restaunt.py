'''
Created on Nov 27, 2015

@author: qiwei
'''
import urllib.request
import json
# CSS_FILTER = 'body > div.ng-scope > div.shopmain.clearfix.container.ng-scope > div.shopmenu.ng-isolate-scope > div.shopmenu-main.grid > div.ng-scope'
URL_ELEME_API = 'http://www.ele.me/restapi/batch'


class ElemeRestaunt():
    '''
    classdocs
    ＠brief Get all eleme restaunt relative information mainly include menu
    '''

    def __init__(self, restaurant_id):
        '''
       
        driver = web_driver()
        driver.get(url)
        time.sleep(3)
    
        element_catelogs = driver.find_elements_by_css_selector(CSS_FILTER)
        for catelog in element_catelogs:
            menus = catelog.find_elements_by_tag_name('div')
            for menu in menus:
                sub_menu = menu.find_elements_by_tag_name('div')
                catelog_title = sub_menu.find_element_by_tag_name('h3').text
                for food in sub_menu:
                    if food.get_attribute('food'):
                        food_id = food.get_attribute('id')
                        try:
                            img = food.find_element_by_tag_name('img')
                            url_img = img.get_attribute('src')
                            print(food_id, url_img)
                        except:
                            pass

                # print(e_title.text)
         '''
        # No Host and Referere here ,otherwise rejected with errorcode=400
        header_dict = {'User-Agent':\
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}

        values = {"timeout":10000,"requests":[{"method":"GET","url":"/v4/restaurants/" +restaurant_id+"/mutimenu"},{"method":"GET","url":"/v1/users/favor/restaurants/"+ restaurant_id}]}
        datas = json.dumps(values)

        url_values = datas.encode(encoding='utf-8')
        # print(url_values)
        request = urllib.request.Request(method="POST", url=URL_ELEME_API, data = url_values, headers=header_dict)
        request.add_header('Accept','application/json, text/plain, */*')  
        #request.add_header('Content-Length', '147')
        
        response = urllib.request.urlopen(request)
        the_page = response.read()
        print(the_page.decode("utf8"))
        
restuane = ElemeRestaunt('389022')        
