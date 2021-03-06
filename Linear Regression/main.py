# -*- coding: utf-8 -*-
"""ml_experiment7_77.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FIH2T1hqomd10xr8Z0Or-LUy_1p8GeO2

# Linear Regression
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df = pd.read_csv("Housing dataset.csv")
df

Y = df[['price']]
X = df.drop(['price', 'id', 'date'],  axis=1)
X.head()

X.info()

df = df.drop(['id', 'date'], axis=1)
df.head()

plt.subplots(figsize=(10,8))
sns.heatmap(df.corr())

"""Linear Regression Implementation using seaborn.regplot() and scipy.stats"""

from scipy import stats
sns.set(color_codes=True)

slope, intercept, r_value, p_value, std_err = stats.linregress(df['sqft_living'],df['price'])

f = plt.figure(figsize=(10,6))
data = df[['price','sqft_living']]
ax = sns.regplot(x='sqft_living', y='price', data=data, 
                 scatter_kws={"color": "g"}, 
                line_kws={'color': 'r', 'label':"y={0:.1f}x+{1:.1f}".format(slope,intercept)})
ax.legend()

"""Linear Regression Implementation using Scikit-Learn."""

x = X[['sqft_living']]
y = Y

xsl = x.values.reshape(-1,1)
ysl = y.values.reshape(-1,1)
xsl = np.concatenate((np.ones(len(xsl)).reshape(-1,1), xsl), axis=1)

from sklearn.linear_model import LinearRegression

slr = LinearRegression()
slr.fit(xsl[:,1].reshape(-1,1), ysl.reshape(-1,1))
y_hat = slr.predict(xsl[:,1].reshape(-1,1))

print('theta[0] = ', slr.intercept_)
print('theta[1] = ', slr.coef_)

thetas = np.array((slr.intercept_, slr.coef_)).squeeze()

plt.figure(figsize=(10,6))
plt.title('$\\theta_0$ = {} , $\\theta_1$ = {}'.format(thetas[0], thetas[1]))
plt.scatter(xsl[:,1],y, marker='x', color='g')
plt.plot(xsl[:,1], np.dot(xsl, thetas), 'r')

print("Slope = ", slope, "\nIntercept = ",intercept)

print("Standard Error = ",std_err)