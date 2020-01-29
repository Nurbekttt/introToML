import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from matplotlib.colors import ListedColormap

dataset = pd.read_csv('wdbc.data')
x = dataset.iloc[:, 2:].values
y = dataset.iloc[:, 1].values

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.20)

sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)

cmap_bold = ListedColormap(['#FF0000', '#00FF00'])

print('KNN classification')

print("acc:",acc)



plt.figure()
plt.scatter(x[:, 1], x[:, 2], c=y, cmap=cmap_bold)
plt.show()



