import requests,os
from fake_useragent import UserAgent

class GateData():
    def __init__(self):
        self.url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11167514849405453471&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%A8%E6%83%85%E5%8C%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=60&rn=30&gsm=3c&1620123979945='
        self.AU = {'User-Agent':UserAgent().random}
        self.name = input('请输入你要爬取的图片名称\n')
        self.num = 1

    def gate(self):
    #百度图片是每30张加载一次，下面代码是默认下载90张，如果想下载更多可以修改第7行range函数中第2个参数可以30往上增加
        for n in range(30,91,30):
            data={
            'tn': 'resultjson_com',
            'logid': '11085831421831146380',
            'ipn': 'rj',
            'ct': '201326592',
            'is':'' ,
            'fp': 'result',
            'queryWord': self.name,
            'cl': '2',
            'lm': '-1',
            'ie':'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': '',
            'z': '',
            'ic': '',
            'hd': '',
            'latest':'' ,
            'copyright': '',
            'word': self.name,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '',
            'istype': '',
            'qc': '',
            'nc': '',
            'fr': '',
            'expermode': '',
            'force': '',
            'pn': n,
            'rn': 30,
            'gsm':'1e',
            '1620122995646': ''
            }
            res = requests.get(url=self.url,headers=self.AU,params=data).json()
            response = res['data']
            for i in response:
                if i != {}:
                    url1 = i['thumbURL']
                    r = requests.get(url=url1).content
                    # 以下代码是下载图片地址，可以根据自己需要保存的路径自行修改
                    if os.path.exists('图片data') == False:
                        os.mkdir('图片data')
                    with open(r'图片data/%s.jpg' % self.num, 'ab') as file:
                        file.write(r)
                    print(url1,'爬取完成%s'%self.num)
                    self.num += 1

r = GateData()
r.gate()
