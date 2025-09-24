# first we will import the require and important libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ReDING THE CSV FILE 
df=pd.read_csv('Iris.csv')  # reading the dat set 
print(df.head())  # checking for the first 5 rows of the data set 
print(df.tail())  # checking for the last 5 rows of the data set 
print(df.info())  # checking for the null values
print(df.describe())  # statistical summary of the data set 
print(df.isnull().sum())  # checking for the missing values
data = df.drop_duplicates(subset ="Species",)
print(data)

# DATA VISUALIZATION
# visualizing the target column 

sns.countplot(x='Species', data=df, )
plt.show()

# relation between the variables
# comparing the sepal length and sepal width 
sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm',
                hue='Species', data=df, )

# Placing Legend outside the Figure
plt.legend(bbox_to_anchor=(1, 1), loc=2)

plt.show()
# comparing the petal length and petal width
sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm',
                hue='Species', data=df, )

# Placing Legend outside the Figure
plt.legend(bbox_to_anchor=(1, 1), loc=2)

plt.show()

#Let's plot all the column's relationships using a pairplot. It can be used for multivariate analysis.
sns.pairplot(df.drop(['Id'], axis = 1), 
             hue='Species', height=2)
plt.show()

#Histograms
#Histograms allow seeing the distribution of data for various columns. It can be used for uni as well as bi-variate analysis.
