import pandas as pd 
import requests as rq 
from bs4  import BeautifulSoup

#blank list

data_list=[]
def getpage(link):
    try:
        page=rq.get(link)
        print('data loaded from =>',link)
        return BeautifulSoup(page.text,'lxml')
    except Exception as e:
        print('error-->',e)

def extract(data):
    target = data.find_all('div',{'class':'_1YokD2 _3Mn1Gg'})[1]
    products = target.find_all('div',{'class':'_1xHGtK _373qXS'})
    size = len(products)
    print("products found =>",size)
    if size > 0:
        for item in products:
            brand =item.find('div',{'class':'_2WkVRV'}).text
            name=item.find('a',{'class':'IRpwTa'}).text
            price=item.find('div',{'class':'_30jeq3'}).text
            try:
                real_price= item.find('div',{'class':'_3I9_wc'}).text
            except:
                real_price= price
            data_list.append({
                                'name':name,'brand':brand,
                                'price':price,'real_price':real_price
                            }) 
        return True
    else:
        print('no product found')
        return False

def save(filepath):
     df = pd.DataFrame(data_list)
     df.to_csv(f'{filepath}.csv') 
     print(f'saved file at {filepath}')


#execution
query='watch'
pos=1
while True:
    url=f'http://www.flipkart.com/search?q={query}&page={pos}'
    print(f'extracting data from {url}....')
    soup=getpage(url)
    if soup:
        status = extract(soup)
        if not status:
            print('Scraping bot finished')
            break
        else:
            pos+=1
    else:
        print('some error error , please look carefully')

save('data') #store in data folder        




