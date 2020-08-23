# 使用BeautifulSoup解析网页
import requests
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/board/4'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for tags in bs_info.find_all('div', attrs={'class': 'movie-item-info'}):
    for atag in tags.find_all('a'):
        #获取电影名称
        print(atag.get('title'))


        #获取详情页链接
        print('https://maoyan.com%s'%atag.get('href'))
        
        #详情页链接
        myurl_detail = 'https://maoyan.com%s'%atag.get('href')
        response_detail = requests.get(myurl_detail,headers=header) 
        bs_info_detail = bs(response_detail.text, 'html.parser')

        #从详情页获取电影类型
        mv_type =''
        for tags_detail in bs_info_detail.find_all('a', attrs={'class':'text-link'}):
                mv_type=mv_type+tags_detail.get_text().strip()+' '
        print(mv_type)         

    for atag in tags.find_all('p', attrs={'class': 'releasetime'}):
        #获取电影名称
        print(atag.get_text())







