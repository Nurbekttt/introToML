import pandas as pd
import seaborn as sns


train = pd.read_csv('titanic_train.csv')
test = pd.read_csv('titanic_test.csv')
s = pd.read_csv('gender_baseline.csv')

data = [train,test]
for training_set in data:
    training_set['Title'] = training_set.name.str.extract(' ([A-Za-z]+)\.', expand=False)
    training_set['Title'] = training_set['Title'].replace(['Dr', 'Rev', 'Col', 'Major', 'Countess', 'Sir', 'Jonkheer', 'Lady', 'Capt', 'Don'], 'Others')
    training_set['Title'] = training_set['Title'].replace('Ms', 'Miss')
    training_set['Title'] = training_set['Title'].replace('Mme', 'Mrs')
    training_set['Title'] = training_set['Title'].replace('Mlle', 'Miss')
    training_set['embarked']=training_set['embarked'].fillna('S')
    training_set['embarked'] = training_set['embarked'].map({'C':0, 'Q':1, 'S':2})
    training_set['sex'] = training_set['sex'].map({'male':0, 'female':1})
    training_set['Title'] = training_set['Title'].map({'Master':0,'Miss':1,'Mr':2,'Mrs':3,'Others':4})
    training_set['age'] = training_set['age'].fillna((training_set['age'].median()))
    training_set.drop(["name","ticket","home.dest","cabin","boat","body"],axis=1,inplace=True)
    training_set['fare'] = training_set['fare'].fillna((training_set['fare'].median()))

s = s.drop(test[test.isnull().any(axis=1)].index)
test = test.drop(test[test.isnull().any(axis=1)].index)
result = test.iloc[:,0]
print(train.isnull().sum())
print(result)
sns.factorplot('survived',data=train,kind='count',hue='pclass')

y_train = train['survived']
x_train = train.drop('survived',axis=1)

y_test = s['survived']
x_test = test
test
sns.factorplot('pclass',data=train,hue='sex',kind='count')

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(x_train,y_train)
print(logmodel.score(x_test,y_test))
y_pred = logmodel.predict(x_test)

df = pd.DataFrame(dict(PassengerId = result,Survived = y_pred)).reset_index()
df.drop('index',axis = 1,inplace = True)
df.to_csv('result.csv',index=False)

