'''
Created on Nov 27, 2015

@author: qiwei
'''
import time
from spider.utility import *

CSS_FILTER = 'body > div.ng-scope > div.shopmain.clearfix.container.ng-scope > div.shopmenu.ng-isolate-scope > div.shopmenu-main.grid > div.ng-scope'


class ElemeRestaunt():
    '''
    classdocs
    ＠brief Get all eleme restaunt relative information mainly include menu
     e_ is shortcut of element_ in selenium
    '''

    def __init__(self, url, _driver):
        '''
        @param url: URL of restaunt
        @param driver: web_driver of elenium
        Constructor
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
