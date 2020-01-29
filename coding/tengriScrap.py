tags=['Изнасилование','избиение']
site="https://tengrinews.kz/tag/"
site1="https://tengrinews.kz/tag/избиение/"
site2="https://tengrinews.kz/tag/Изнасилование/"
import requests
import pandas as pd
from bs4 import BeautifulSoup
date=[]
location=[]
cities=["Алма","Нур-Султан","Шымкент","Актоб","Караганд","Тараз","Павлодар","Усть-Каменогорск","Семей","Атыра","Костана","Кызылорд","Уральск","Петропавловск","Актау","Темиртау","Туркестан","Кокшетау","Талдыкорган","Экибастуз","Рудн"]
cities1=["Алма-ата","Нур-Султан","Шымкент","Актобе","Караганда","Тараз","Павлодар","Усть-Каменогорск","Семей","Атырау","Костанай","Кызылорда","Уральск","Петропавловск","Актау","Темиртау","Туркестан","Кокшетау","Талдыкорган","Экибастуз","Рудный"]
tag=[]
for t in tags:
    for i in range(1,20):
        params = {"page":i}
        r = requests.get(site+t, params=params)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        searches=soup.find_all('div', attrs={'class':'search-result'})
        for i in searches:
            
            
                if("2019" in i.find('span').text):
                    z=0
                    for index in range(len(cities)):
                        if cities[index] in i.text:
                            print(cities1[index])
                            if(z==0):
                                location.append(cities1[index])
                            z=1
                    if z:
                        date.append(i.find('span').text)
                        tag.append(t) 
                        print(i.find('span').text)
                    else:
                        date.append(i.find('span').text)
                        location.append("null")
                        tag.append(t)

                elif("12.2018" in i.find('span').text):
                    z=0
                    for index in range(len(cities)):
                        if cities[index] in i.text:
                            print(cities1[index])
                            if(z==0):
                                location.append(cities1[index])
                            z=1
                    if z:
                        date.append(i.find('span').text)
                        tag.append(t) 
                        print(i.find('span').text)
                    else:
                        date.append(i.find('span').text)
                        location.append("null")
                        tag.append(t)

                elif("11.2018" in i.find('span').text):
                    z=0
                    for index in range(len(cities)):
                        if cities[index] in i.text:
                            print(cities1[index])
                            if(z==0):
                                location.append(cities1[index])
                            z=1
                    if z:
                        date.append(i.find('span').text)
                        tag.append(t) 
                        print(i.find('span').text)
                    else:
                        date.append(i.find('span').text)
                        location.append("null")
                        tag.append(t)                    
print(len(location),len(date),len(tag))
df = pd.DataFrame({'Location': location,'Date': date,'Tag': tag})
df.to_csv("tengri.csv")
