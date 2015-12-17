'''
Created on Dec 8, 2015

@author: qiwei
'''
import urllib.request
import json
import http.cookiejar

IMAGE_URL = 'https://account.ele.me/restapi/v1/captchas/'

cookie = http.cookiejar.CookieJar()
cookieProc = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookieProc)
urllib.request.install_opener(opener)
print(cookie)
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

    def url_image_of_verificaiton(self):
        '''
            Get the url of verification image
        '''

        request = urllib.request.Request(method="POST", url=self.URL_VERIFICATION_IMAGE, headers=self.HEADER_DICT)
        request.add_header('Accept', 'application/json, text/plain, */*')
        response = urllib.request.urlopen(request)
        # print(response.info())
        response = json.loads(response.read().decode('utf-8'))
        url_image = IMAGE_URL + response['code']
        # (file_local, header) = urllib.request.urlretrieve(url_image)
        # print(file_local)
        return url_image

    def login(self, user, password, verificaion_code):
        '''
            Try to login and return response
            @return {'success':True,'error':''}
        '''
        values = {'username': str(user), 'password': str(password), 'captcha_code': str(verificaion_code)}
        datas = json.dumps(values)
        url_values = datas.encode(encoding='utf-8')

        request = urllib.request.Request(method="POST", url=self.URL_LOGIN, data=url_values, headers=self.HEADER_DICT)
        request.add_header('Accept', 'application/json, text/plain, */*')

        try:
            response = urllib.request.urlopen(request)
            # print(response.info())
        except urllib.error.HTTPError as e:
            error = e.read()
            print(error)
            return {'success': False, 'info': str(error)}
        response = json.loads(response.read().decode('utf-8'))

        '''
        for ck in cookie:
            print(ck.name,':',ck.value)
        '''
        self.user_id = response['user_id']
        return {'success': True, 'info': response}
