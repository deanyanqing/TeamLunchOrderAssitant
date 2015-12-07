'''
Created on Dec 8, 2015

@author: qiwei
'''
import urllib.request
import json
import http.cookiejar

IMAGE_URL = 'https://account.ele.me/restapi/v1/captchas/'


class ElemeLogin():
    '''
    Step 1: Involke image_of_verificaiton to get verification image_of_verificaiton
    Step 2: Login with username,passwd,code
    '''
    URL_VERIFICATION_IMAGE = 'https://account.ele.me/restapi/v1/captchas'
    URL_LOGIN = 'https://account.ele.me/restapi/v1/login'
    HEADER_DICT = {'User-Agent':
                       'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}
    def __init__(self):
        pass

    '''
    Get the url of verification image
    '''
    def url_image_of_verificaiton(self):
        cookie = http.cookiejar.CookieJar() 
        cookieProc = urllib.request.HTTPCookieProcessor(cookie) 
        opener = urllib.request.build_opener(cookieProc) 
        urllib.request.install_opener(opener) 
        
        request = urllib.request.Request(method="POST", url=self.URL_VERIFICATION_IMAGE, headers=self.HEADER_DICT)
        request.add_header('Accept', 'application/json, text/plain, */*')
        response = urllib.request.urlopen(request)
        print(response.info())
        response = json.loads(response.read().decode('utf-8'))
        url_image = IMAGE_URL + response['code']
        # print(image)

        # (file_local, header) = urllib.request.urlretrieve(url_image)
        # print(file_local)
        return url_image
    
    def login(self, user, password, verificaion_code):
        values = {'username':str(user), 'password': str(password), 'captcha_code': str(verificaion_code)}
        datas = json.dumps(values)
        url_values = datas.encode(encoding='utf-8')
        
        request = urllib.request.Request(method="POST", url=self.URL_LOGIN, data=url_values, headers=self.HEADER_DICT)
        request.add_header('Accept', 'application/json, text/plain, */*')
        
        try:
            response = urllib.request.urlopen(request)
            # print(response.info())
        except urllib.error.HTTPError as e:
            print( e.read())
        response = json.loads(response.read().decode('utf-8'))
        # print(response)

#login = ElemeLogin()
#login.url_image_of_verificaiton()