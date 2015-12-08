'''
Created on Nov 23, 2015

@author: qiwei
'''
from spider.eleme_nearby_restaunts import ElemeNearbyRestauntManager


# restaunt_manager = RestauntsManager('shanghai')
# restaunt_manager.dump()
# restaunt_manager.refresh_all_restaunt()

# restaunt = ElemeRestaunt()
neayRestuantsMgr = ElemeNearbyRestauntManager()
restaunts = neayRestuantsMgr.restuants('')
r = neayRestuantsMgr.restaunt_object(restaunts[0]['id'])
r.load_menu()
