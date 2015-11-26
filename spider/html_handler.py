'''
Created on Oct 23, 2015

@author: qiwei
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request  
import urllib.parse 
from urllib.error import URLError,HTTPError  
from bs4 import BeautifulSoup
import re
import json
from spider.food import  FoodCatalogue
import os
class HtmlHandler():
    #mealRecordRe = re.compile("^food_view_\d+")
    #foodRe=re.compile(r'class="rst-d-name food_name" title="(\S+)"' )
    #priceRe = re.compile('class="price symbol-rmb">(\d+)<')
    #addActionIndexRe = re.compile(r'role="button" ubt-click="(\d+)"><span class')
    #orderStatusRe = re.compile(r'class="icon-d-star s\d+ i_s"></i>\((\d*)\)</span><br><span class="rst-d-sales">([^<]+)')
    jsonRe = re.compile('JSON.parse\("(\[[^;]+\])"\);')
    restaurantTitleRe = re.compile('href="([^"]+)" itemprop="name" title="([^"]+)"')
    restaurantRakingRe = re.compile('class="glyph-rating-star">.</i></span>([^<]+)')
    restaurantLogoRe = re.compile('data-srcset="([^"]+)"')
    restaurantPremiumRakingRe = re.compile('<span itemprop="ratingValue">([^<]+)<')
    dataSrcDir=os.path.join(os.environ['HOME'],'lunchRes','image')
    def __init__(self,url):
        print(url)
        header_dict={'User-Agent':\
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'} 
        values={'wd':'python',  
        'opt-webpage':'on',  
        'firefox':'gbk'}  
        url_values=urllib.parse.urlencode(values)
        url_values=url_values.encode(encoding='UTF8')  
        full_url=urllib.request.Request(url=url,headers = header_dict)
        #print(full_url)  
        try:
            local_filename, headers =urllib.request.urlretrieve(url) 
            print(local_filename)
            #image = urllib.request.urlretrieve('http://fuss10.elemecdn.com/4/fd/79bbfef067ca07f7b4679e3b53d98jpg.jpg')
            #print(image)
            #local_filename = "/tmp/tmpnmbj6suj" 
            self.file = local_filename

        except HTTPError as e:  
            print('Error code:',e.code)   
        except URLError as e:  
            print('Reason',e.reason) 
    
    def getFile(self,url):
        print("getFile")
     
    def getLocalHtml(self):
        return self.file 
   
    def getBasicRestauntInfo(self):
        print("getBasicRestauntInfo")
        soup = BeautifulSoup(open(self.file),"html.parser")  
        header = soup.find_all("header",class_='rst-header-info group')
        if  header:            
            print(type(header))
            (hurl,name) = self.restaurantTitleRe.search(str(header)).group(1,2)
            #print(name)
            imageUrl = self.restaurantLogoRe.search(str(header)).group(1)
            image = urllib.request.urlretrieve(imageUrl,self.dataSrcDir+'/'+name +'.jpg')
            #print(image)
            raking = self.restaurantRakingRe.search(str(header)).group(1)
        else:
            header = soup.find_all("header",class_='rst-header-info group premium')
            print(header)
            (hurl,name) = self.restaurantTitleRe.search(str(header)).group(1,2)
            #print(name)
            imageUrl = self.restaurantLogoRe.search(str(header)).group(1)
            image = urllib.request.urlretrieve(imageUrl,self.dataSrcDir+'/'+name +'.jpg')
            #print(image)
            rating_point_header =soup.find_all("div",class_='rating-point header')
            raking = self.restaurantPremiumRakingRe.search(str(rating_point_header)).group(1)
            
        return (image,name,raking.strip())
        
        
    def phaseJson(self,jsonStr):
        print("phasejson")
        catalogsObj=[]
        jsonInput =self.jsonRe.search(jsonStr)
        if jsonInput:
            j = jsonInput.group(1)  
            
            #remove unneeded special format in javascript         
            j = j.replace('\\"','"')
            jsonRaw = j.replace("\\\\","\\")
            
            catalogas = json.loads(jsonRaw, encoding="utf-8")
            #print(len(catalogas))
            for catalog in catalogas:
                foodCatalog=FoodCatalogue(catalog)
                catalogsObj.append(foodCatalog)
        return  catalogsObj
    
    def phaseSection(self,food):
        print("phaseSection")
        name = self.foodRe.search(str(food)).group(1)
        print(name)
        if -1 != name.find("二维码"):
            return []
        price = self.priceRe.search(str(food)).group(1)
        print(price)
        match = self.orderStatusRe.search(str(food))
        if match:
            print(match.group(1,2))

    def phaseHtml(self):  
        soup = BeautifulSoup(open(self.file),"html.parser")  
        #table = soup.find_all("div", id="cate_view")
        #foods = soup.find_all("li",id=self.mealRecordRe)
        #print(len(foods))
        #for food in foods:
        #    dishes = self.phaseSection(food)
        allScripts = soup.find_all("script",type='text/javascript')
        for s in allScripts:
            if -1 != str(s).find("menu = JSON.parse"):
                return self.phaseJson(str(s))
        return []      
