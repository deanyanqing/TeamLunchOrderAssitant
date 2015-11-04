'''
Created on Jun 1, 2015

@author: qiwei
'''

'''
import urllib2  
import urllib  
import cookielib  
import codecs

class Login(object):

    def __init__(self, user,passwd,loginUrl):
        '''
        Constructor
        '''
        try:  
            cj = cookielib.CookieJar()  
            opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
            opener.addheaders = [('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0')]  
            urllib2.install_opener(opener) 

            data = urllib.urlencode({'txtAccount':'elina.chen@careerfocus.com.cn','txtPassword':'fazhan1224'})  
            request = urllib2.Request(loginUrl, data)
            result = urllib2.urlopen(request)  
            result.read() 
'''            