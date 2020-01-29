import requests
import matplotlib.pyplot as plt
import numpy as np

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
while amount<100:
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
        if amount==100:
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



#for first plot
d1={}
d2={}
for i in range(len(dictionary["room"])):
    print(dictionary["area"][i])
    tgOfM=int(dictionary["price"][i].replace("\xa0", ""))/float(dictionary["area"][i])
    if dictionary["room"][i] not in d1.keys():
        d1[dictionary["room"][i]]=[tgOfM]
        d2[dictionary["room"][i]]=1
    else:
        d1[dictionary["room"][i]].append(tgOfM)
        d2[dictionary["room"][i]]+=1

y_pos=[]

for i in arrRoom:
    y_pos.append(np.average(d1[i]))

print(arrRoom)

# Fixing random state for reproducibility
#np.random.seed(19680801)


#plt.rcdefaults()
fig, ax = plt.subplots()




#ax.barh(arrRoom, y_pos,  align='center')
#ax.set_yticks(y_pos)
#ax.set_yticklabels(arrRoom)
#ax.invert_yaxis()  # labels read top-to-bottom
#ax.set_xlabel('₸/m²')
#plt.yticks(np.arange(0, 5000, 10))
#ax.set_title("that's how much you pay per m2")

#plt.show()



#for second plot
y2=[]
print(len(arrRoom))
for i in arrRoom:
    y2.append(d2[i])
N = 5
menMeans = (20, 35, 30, 35)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(len(arrRoom))    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

plt.bar(ind, y2, width)
#p2 = plt.bar(ind, womenMeans, width,bottom=menMeans, yerr=womenStd)

plt.ylabel('Apartments')
plt.title('')
plt.xlabel("Number of rooms")
plt.xticks(ind, arrRoom)
plt.yticks(np.arange(0, 50, 5))
#plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()

