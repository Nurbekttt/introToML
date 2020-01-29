import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d


cities=["Алма-ата","Нур-Султан","Шымкент","Актобе","Караганда","Тараз","Павлодар","Усть-Каменогорск","Семей","Атырау","Костанай","Кызылорда","Уральск","Петропавловск","Актау","Темиртау","Туркестан","Кокшетау","Талдыкорган","Экибастуз","Рудный"]
df = pd.read_csv('tengri.csv')
locs=[]
for i in df['Location']:
    locs.append(i)
val=[]
for city in cities:
    val.append(locs.count(city))
    
dates=[]
valDate=[]
for date in df['Date']:
    dates.append(i)
val=[]
for city in cities:
    val.append(locs.count(city))

plt.figure(figsize=(20, 3))

plt.bar(cities, val)

plt.suptitle('Categorical Plotting')
plt.show()


