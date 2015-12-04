'''
Created on Jun 2, 2015

@author: qiwei
'''
import urllib.request
import os


class Food():
    '''
    classdocs
    '''

    imagesUrl = 'http://fuss10.elemecdn.com'
    dataSrcDir = os.path.join(os.environ['HOME'], 'lunchRes', 'image')

    def dump(self):
        print([self.name, self.price, self.ratingCount, self.num_ratings, self.sales])

    def getImage(self, imageRelativeUrl):
        image = ''
        imageRelativeUrl = imageRelativeUrl.strip()
        if '' != imageRelativeUrl:
            url = self.imagesUrl + imageRelativeUrl
            print(imageRelativeUrl)
            image = urllib.request.urlretrieve(url, self.dataSrcDir + '/' + self.name + '.jpg')
            print(image)

        return image

    def __init__(self, food):
            # print("init food")
            self.name = food['name']
            self.price = food['price']

            self.ratingCount = food['ratingCount']
            self.num_ratings = food['num_ratings']
            self.attributes = food['attributes']
            self.id = food['id']
            self.sales = food['sales']
            self.stock = food['stock']
            self.pinyinName = food['pinyinName']
            self.impage = self.getImage(food['img'])
            self.description = ''
            self.dump()


class FoodWithImage(Food):

    def __init__(self, food):
        print("init FoodwithImage")
        self.impage = ''


class FoodCatalogue():

    def getFood(self, foods):
        foodsObj = []
        # print(foods)
        if len(foods) == 0:
            return foodsObj
        # print(foods)
        if len(foods['without_image']) > 0:
            for food in foods['without_image']:
                f = Food(food)
                foodsObj.append(f)
        if len(foods['with_image']) > 0:
            for food in foods['with_image']:
                f = Food(food)
                foodsObj.append(f)
        return foodsObj

    def __init__(self, json):
        # print(json['categId'])
        self.categId = json['categId']
        self.mustNewUser = json['mustNewUser']
        self.description = json['description']
        self.mustPayOnline = json['mustPayOnline']
        self.foods = self.getFood(json['foods'])
        self.categ = json['categ']
        self.isActivity = json['isActivity']

    def dump(self):
        print(self.categId, self.mustNewUser, self.description, self.mustPayOnline, self.categ, self.isActivity)
        for food in self.foods:
            food.dump()
