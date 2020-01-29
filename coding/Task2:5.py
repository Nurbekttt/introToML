import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d

df = pd.read_csv('hw2.csv')
print(df)


heatmap_pivot = pd.pivot_table(df, values='Price', index='Location', columns='# of rooms')
ax23 = sns.heatmap(heatmap_pivot, cmap='Wistia', annot=True)
ax23.collections[0].colorbar.set_label('Price')




fg1 = plt.figure()
sns.countplot(x='Location', data=df)
ax23.set_title('e+07 is like 10^7')


plt.show()
print(df.describe())
