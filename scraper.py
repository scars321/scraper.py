from bs4 import BeautifulSoup
import requests


header ={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url='LINK'
response=requests.get(url,headers=header)

#print(response.content)

soup=BeautifulSoup(response.content, 'lxml')

for item in soup.find_all('tr'):
    if item.select('.storylink'):
        print(item.select('.storylink')[0].get_text())
        print(item.select('.storylink')[0]['href'])
        print("________________")

    if item.select('.score'):
        print(item.select('.score')[0].get_text())
        

       
    
