import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl


df = pd.read_csv(r"C:\Users\apjad\Desktop\Salary_DATA.csv")
print(df.describe)


plt.scatter(df.YearsExperience, df.Salary, color="red")
plt.xlabel("Years Experience")
plt.ylabel("Salary")

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import linear_model

x = df.iloc[:,0].values
y = df.iloc[:,-1].values
print(x.head())
print(y.head())
#split the dataset
 
X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.2, random_state=0)

train_x = np.asanyarray(X_train)
train_y = np.asanyarray(Y_train)
regr = linear_model.LinearRegression()
regr.fit (train_x.reshape(-1,1),train_y)

print('Coefficients : ', regr.coef_)
print('Intercept : ',regr.intercept_)
train_y.shape


from sklearn.linear_model import LinearRegression
regr=LinearRegression()
regr.fit(X_train,Y_train)

#Predicting the test set results
y_pred = regr.predict(X_test)
plt.scatter(X_train,Y_train,color='red')
plt.plot (X_train,regr.predict(X_train),color='blue')

plt.tittle('salary vs Experience (train set)')
plt.xlabel('years of Experience')
plt.ylabel('salary')
plt.show()
