import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score
import seaborn as sns
from matplotlib import pyplot as plt
df = pd.read_csv('amazon_cells_labelled.txt', names=['sentence', 'posOrNeg'], sep='\t')
cv = CountVectorizer(strip_accents='ascii', token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b', lowercase=True, stop_words='english')
X = df['sentence']
ylabels = df['posOrNeg']

X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=0.3)
#print(X, ylabels)
X_train_cv = cv.fit_transform(X_train)
X_test_cv = cv.transform(X_test)
#print(len(X_train),"aaaa")
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train_cv, y_train)    
predictions = naive_bayes.predict(X_test_cv)                                                        

print('Accuracy score: ', accuracy_score(y_test, predictions))
print('Precision score: ', precision_score(y_test, predictions))


comment = cv.transform(["This is the best explanation of the Laplace smoothing method I have found in hours of searching. Thank you so much!!!"])
predict = naive_bayes.predict(comment)
print(predict)
comment = cv.transform(['this is very good'])
predict = naive_bayes.predict(comment)
print(predict)

comment = cv.transform(['this is awful'])
predict = naive_bayes.predict(comment)
print(predict)



import requests  
r = requests.get('https://www.imdb.com/title/tt7286456/reviews?ref_=tt_urv')

from bs4 import BeautifulSoup  
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('div', attrs={'class':'text show-more__control'})
arr=[]
q=0
for i in results:
    s=str(i)[(str(i).find(">"))+1:(str(i).find("</"))]
    comment = cv.transform([s])
    predict = naive_bayes.predict(comment)
    
    arr.append(predict)
    if predict==[0] and q==0:
        print(s)
        q=1
        
liked = 0
disliked = 0
for i in arr:
    if(i==[1]):
        liked+=1
    else:
        disliked+=1
print("positive comments of movie 'Joker' from https://www.imdb.com",liked/(len(arr)))






