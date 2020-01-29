import requests  
r = requests.get('https://m.krisha.kz/arenda/kvartiry/?das[rent.period]=2')

from bs4 import BeautifulSoup  
soup = BeautifulSoup(r.text, 'html.parser')
dictionary={}
dictionary["number"]=[]
dictionary["area"]=[]
dictionary["floor"]=[]
dictionary["price"]=[]
amount=0
page=2
print(soup)
while amount<1000:
    results = soup.find_all('a', attrs={'class':'a-card__title'})
    prices = soup.find_all('span', attrs={'class':'a-card__price-text'})
    index=0
    
    for i in results:
        area=str(i)[str(i).find(",")+2:str(i).find("м²")-1]
        dictionary["area"].append(area)
        floor=str(i)[str(i).find("м²,")+4:str(i).find("этаж")-1]
        if(floor.find('class')==-1):
            dictionary["floor"].append(floor)
        else:
            dictionary["floor"].append("1")
        price=str(prices[index])[str(prices[index]).find(">")+1:str(prices[index]).find("<",1)-1]
        dictionary["price"].append(price)
        
        index+=1
        amount+=1

        dictionary["number"].append(amount)
        if amount==1000:
            break
    r = requests.get('https://m.krisha.kz/arenda/kvartiry/?das[rent.period]=2&page='+str(page))
    soup = BeautifulSoup(r.text, 'html.parser')
    page+=1
    print(page,"/",amount)
records = []

import pandas as pd  
df = pd.DataFrame(data=dictionary)
print(df)
df.to_csv('hw1.csv', index=False, encoding='utf-8') 
