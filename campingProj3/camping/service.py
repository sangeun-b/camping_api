import json
import requests
from urllib import parse
from bs4 import BeautifulSoup

class CampingService:

    def __init__(self):
        self.url = ''
        self.key = ''
        self.page = 1
        self.clist = []

    def saveVo(self, data):
        dkey = ['facltNm', 'lineIntro', 'intro', 'manageSttus', 'featureNm', 'doNm', 'sigungNum', 'addr1', 'addr2', 'mapX', 'mapY', 'direction', 'tel', 'homepage',
                'resveUrl','gnrlSiteCo', 'autoSiteCo', 'glampSiteCo', 'caravSiteCo', 'indvdlCaravSiteCo', 'sbrsCl', 'sbrsEtc', 'animalCmgCl','firstImageUrl']
        list = []
        for d in data:
            vo2 = {}
            for i,dk in enumerate(dkey):
                for key in d:
                    ck = False
                    list2 = []
                    if dk in key:
                        ck = True
                        break
                    else:
                        if dk not in list2:
                            list2.append(dk)
                if ck == False:
                    vo2[dk] = 'None'
                else:
                    vo2[dk] = d[dk]
            list.append(vo2)

        for i, li in enumerate(list):
            print(i,li)
        return list

    def getOne(self,data,facltNm):
        dkey = ['facltNm', 'lineIntro', 'intro', 'manageSttus', 'featureNm', 'doNm', 'sigungNum', 'addr1', 'addr2',
                'mapX', 'mapY', 'direction', 'tel', 'homepage',
                'resveUrl', 'gnrlSiteCo', 'autoSiteCo', 'glampSiteCo', 'caravSiteCo', 'indvdlCaravSiteCo', 'sbrsCl',
                'sbrsEtc', 'animalCmgCl', 'firstImageUrl']

        for d in data:
            if facltNm.strip() == d['facltNm'].strip():
                res = {}
                for i, dk in enumerate(dkey):
                    for key in d:
                        ck = False
                        if dk in key:
                            ck = True
                            break

                    if ck == False:
                        res[dk] = 'None'
                        # print(res[dk])
                    else:
                        res[dk] = d[dk]
        return res

    def getCamping(self,pageNo):
        self.url = 'http://api.visitkorea.or.kr/openapi/service/rest/GoCamping/basedList?'
        self.key = 'HP6X0ANLG4fD7izU7D5NLt62p%2FFWoioo%2BlObIBdA6AjC1UdonTMZsPI%2Brhtf7XZo3TvXhcywJZJ6M%2BFLrPtxVA%3D%3D'
        self.url += 'ServiceKey=' + self.key
        pageNo = pageNo
        self.url += '&numOfRows=10&pageNo=' + str(pageNo)
        self.url += '&MobileOS=ETC&MobileApp=TestApp&_type=json'
        html = requests.get(self.url).text
        res = json.loads(html)
        print(html)
        data = res['response']
        data = data['body']
        data = data['items']
        data = data['item']
        res = []
        res = self.saveVo(data)
        return res

    def getNextPage(self,pageNo):
        self.url = 'http://api.visitkorea.or.kr/openapi/service/rest/GoCamping/basedList?'
        self.key = 'HP6X0ANLG4fD7izU7D5NLt62p%2FFWoioo%2BlObIBdA6AjC1UdonTMZsPI%2Brhtf7XZo3TvXhcywJZJ6M%2BFLrPtxVA%3D%3D'
        self.url += 'ServiceKey=' + self.key
        pageNo += 1
        self.url += '&numOfRows=10&pageNo='+str(pageNo)
        self.url += '&MobileOS=ETC&MobileApp=TestApp&_type=json'

        html = requests.get(self.url).text
        res = json.loads(html)
        data = res['response']
        data = data['body']
        data = data['items']
        data = data['item']
        res = []
        res = self.saveVo(data)
        return pageNo,res

    def getPrePage(self,pageNo):
        self.url = 'http://api.visitkorea.or.kr/openapi/service/rest/GoCamping/basedList?'
        self.key = 'HP6X0ANLG4fD7izU7D5NLt62p%2FFWoioo%2BlObIBdA6AjC1UdonTMZsPI%2Brhtf7XZo3TvXhcywJZJ6M%2BFLrPtxVA%3D%3D'
        self.url += 'ServiceKey=' + self.key
        pageNo -= 1
        self.url += '&numOfRows=10&pageNo=' + str(pageNo)
        self.url += '&MobileOS=ETC&MobileApp=TestApp&_type=json'

        html = requests.get(self.url).text
        res = json.loads(html)
        data = res['response']
        data = data['body']
        data = data['items']
        data = data['item']
        res = []
        res = self.saveVo(data)
        return pageNo, res

    def getDetail(self,pageNo,facltNm):
        self.url = 'http://api.visitkorea.or.kr/openapi/service/rest/GoCamping/basedList?'
        self.key = 'HP6X0ANLG4fD7izU7D5NLt62p%2FFWoioo%2BlObIBdA6AjC1UdonTMZsPI%2Brhtf7XZo3TvXhcywJZJ6M%2BFLrPtxVA%3D%3D'
        self.url += 'ServiceKey=' + self.key
        self.url += '&numOfRows=10&pageNo=' + str(pageNo)
        self.url += '&MobileOS=ETC&MobileApp=TestApp&_type=json'
        print(self.url)
        html = requests.get(self.url).text
        res = json.loads(html)
        data = res['response']
        data = data['body']
        data = data['items']
        data = data['item']
        res = self.getOne(data,facltNm)
        return res


    def getCampByaddr(self, addr):
        self.url = 'http://api.visitkorea.or.kr/openapi/service/rest/GoCamping/basedList?'
        self.key = 'ekde%2BjriV1xwCQEu5ZXb9crsoWrSBKXGkgeWBSscRS8jeaZ51rYplwcXojkZb0JtVY5LvFpfrhZk0bG9VAvWhw%3D%3D'
        self.url += 'ServiceKey=' + self.key
        self.url += '&numOfRows=2910&pageNo=1'
        self.url += '&MobileOS=ETC&MobileApp=TestApp&_type=json'

        html = requests.get(self.url).text
        res = json.loads(html)
        response = res['response']
        body = response['body']
        items = body['items']
        data = items['item']

        self.clist.clear()
        for c in data:
            if addr.strip() in c['addr1'].strip():
                dkey = ['facltNm', 'lineIntro', 'intro', 'manageSttus', 'featureNm', 'doNm', 'sigungNum', 'addr1',
                        'addr2', 'mapX', 'mapY', 'direction', 'tel', 'homepage',
                        'resveUrl', 'gnrlSiteCo', 'autoSiteCo', 'glampSiteCo', 'caravSiteCo', 'indvdlCaravSiteCo',
                        'sbrsCl', 'sbrsEtc', 'animalCmgCl', 'firstImageUrl']
                vo2 = {}
                for i, dk in enumerate(dkey):
                    for key in c:
                        ck = False
                        if dk in key:
                            ck = True
                            break

                    if ck == False:
                        vo2[dk] = 'None'
                    else:
                        vo2[dk] = c[dk]
                self.clist.append(vo2)

        return self.clist


    def getCampByName(self, keyword):
        self.url = 'http://api.visitkorea.or.kr/openapi/service/rest/GoCamping/searchList?'
        self.key = 'ekde%2BjriV1xwCQEu5ZXb9crsoWrSBKXGkgeWBSscRS8jeaZ51rYplwcXojkZb0JtVY5LvFpfrhZk0bG9VAvWhw%3D%3D'
        self.url += 'ServiceKey=' + self.key
        self.url += '&MobileOS=ETC&MobileApp=AppTest&_type=json'

        keyword2 = parse.quote(keyword)

        self.url += '&keyword=' + keyword2
        html = requests.get(self.url).text
        res = json.loads(html)
        response = res['response']
        body = response['body']
        items = body['items']
        data = items['item']
        self.clist.clear()
        for c in data:
            print('이름검색:',c)
            if keyword.strip() in c['facltNm'].strip():
                dkey = ['facltNm', 'lineIntro', 'intro', 'manageSttus', 'featureNm', 'doNm', 'sigungNum', 'addr1',
                        'addr2', 'mapX', 'mapY', 'direction', 'tel', 'homepage',
                        'resveUrl', 'gnrlSiteCo', 'autoSiteCo', 'glampSiteCo', 'caravSiteCo', 'indvdlCaravSiteCo',
                        'sbrsCl', 'sbrsEtc', 'animalCmgCl', 'firstImageUrl']
                vo2 = {}
                for i, dk in enumerate(dkey):
                    for key in c:
                        ck = False
                        if dk in key:
                            ck = True
                            break

                    if ck == False:
                        vo2[dk] = 'None'
                    else:
                        vo2[dk] = c[dk]
                self.clist.append(vo2)
        return self.clist

    def getDetailBySearch(self,facltNm):
        c = {}
        for cl in self.clist:
            if facltNm.strip() == cl['facltNm'].strip():
                c =cl
        return c




