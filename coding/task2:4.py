import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

r = requests.get('https://m.krisha.kz/arenda/kvartiry/?das[rent.period]=2')

from bs4 import BeautifulSoup  
soup = BeautifulSoup(r.text, 'html.parser')
dictionary={}
dictionary["number"]=[]
dictionary["area"]=[]
dictionary["floor"]=[]
dictionary["price"]=[]
dictionary["room"]=[]
amount=0
page=2
while amount<1:
    results = soup.find_all('a', attrs={'class':'a-card__title'})
    prices = soup.find_all('span', attrs={'class':'a-card__price-text'})
    index=0
    
    for i in results:
        
        room=int(str(i)[str(i).find(">")+1:str(i).find("-комнат")])
        
        dictionary["room"].append(room)
        area=str(i)[str(i).find(",")+2:str(i).find("м²")-1]
        dictionary["area"].append(area)
        floor=str(i)[str(i).find("м²,")+4:str(i).find("этаж")-1]
        if(floor.find('class="a-card__title link"')==-1):
            dictionary["floor"].append(floor)
        else:
            dictionary["floor"].append("-")
        price=str(prices[index])[str(prices[index]).find(">")+1:str(prices[index]).find("<",1)-1]
        dictionary["price"].append(price)
        
        index+=1
        amount+=1

        dictionary["number"].append(amount)
        if amount==1:
            break
    r = requests.get('https://m.krisha.kz/arenda/kvartiry/?das[rent.period]=2&page='+str(page))
    soup = BeautifulSoup(r.text, 'html.parser')
    page+=1
records = []

arrRoom=[]
for i in dictionary["room"]:
    if not i in arrRoom:
        arrRoom.append(i)
arrRoom.sort()


df = pd.read_csv('hw2.csv')
#for first plot
d1={}
d2={}
for i in range(len(dictionary["room"])):
    
    if dictionary["room"][i] not in d1.keys():
        d1[dictionary["room"][i]]=[float(dictionary["area"][i])]
        d2[dictionary["room"][i]]=1
    else:
        d1[dictionary["room"][i]].append(float(dictionary["area"][i]))
        d2[dictionary["room"][i]]+=1

y_pos=[]

fig3 = plt.figure()
#fig3_1 = fig3.add_subplot(2,1,1)
#fig3_1.scatter(dictionary['area'], dictionary['price'], color='red')
#fig3_1.set_xlabel('area')
#fig3_1.set_ylabel('price')

prices = []
for i in range(len(df.Price)):
    prices.append(int(df.Price[i]))
print("aaa",prices)
prices.sort()
fig3_2 = fig3.add_subplot()
fig3_2.scatter(df["# of rooms"], df.Price, color='green')
fig3_2.set_xlabel('number of rooms')
fig3_2.set_ylabel('price')



plt.show()
