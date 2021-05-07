import requests,pandas
from fake_useragent import UserAgent

class GetData():
    def __init__(self):
        self.url = 'http://fund.eastmoney.com/js/fundcode_search.js?v=20210506123001'
        self.UA = {'User-Agent':UserAgent().random}
#爬取数据
    def get(self):
        response = requests.get(url=self.url,headers=self.UA).text
        res=response.replace('var r = [','')
        res=res.replace('];','')
        return eval(res)
#处理数据并保存到CSV
    def data(self,res):
        list1 = []
        list2 = []
        list3 = []
        for i in res:
            list1.append('代码：'+i[0])   # 因为i[0]是数据保存在表格时前面的0会默认消失，所以前面加写内容
            list2.append(i[2])
            list3.append(i[3])
        df = pandas.DataFrame(columns=['基金代码','基金名称','基金类型'])
        df['基金代码']=list1
        df['基金名称']=list2
        df['基金类型']=list3
        print(df)
        df.to_csv('./基金.csv')

if __name__ == '__main__':
#实例化类对象并调用类方法
    r=GetData()
    res = r.get()
    r.data(res)
