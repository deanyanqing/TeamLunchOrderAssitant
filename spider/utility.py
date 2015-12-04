'''
Created on Nov 24, 2015

@author: qiwei
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from spider.generate_chrome_proxy import generate_chrome_proxy
import os.path
from spider.check_proxy import has_proxy


def _web_driver_no_proxy():
    driver = webdriver.Firefox()
    return driver


def _web_driver_with_proxy():
        # fix proxy problem
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference("network.proxy.type", 1);
        # profile.set_preference('network.proxy.http', "114.66.81.130")
        # profile.set_preference("network.proxy.http_port", 8080);
        # driver = webdriver.Firefox(firefox_profile=profile)

    pluginfile = 'proxy_auth_plugin.zip'
    if False == os.path.exists(pluginfile):
        generate_chrome_proxy()

    co = Options()
    co.add_argument("--start-minimized")
    co.add_extension(pluginfile)

    driver = webdriver.Chrome(chrome_options=co)
    return driver

def web_driver():
    if has_proxy():
        return _web_driver_with_proxy()
    else:
        return _web_driver_no_proxy()
