


# Code source: Jaques Grobler
# License: BSD 3 clause

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('hw2.csv')


# Split the data into training/testing sets
diabetes_X_train = df.Area.values[:5000].reshape(-1,1)
diabetes_X_test = df.Area.values[5000:].reshape(-1,1)


diabetes_y_train = df.Price.values[:5000].reshape(-1,1)
diabetes_y_test = df.Price.values[5000:].reshape(-1,1)


regr = linear_model.LinearRegression()


regr.fit(diabetes_X_train, diabetes_y_train)


diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_train, diabetes_y_train,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=2)
plt.ylabel('price')
plt.xlabel('area')
plt.show()
