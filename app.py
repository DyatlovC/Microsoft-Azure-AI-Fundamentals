import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("IceCreams.csv")  # Training Data

modelo = LinearRegression()

"""
Split the training data randomly to create a data set with wich to train the model 
"""
y = df[["Temperature"]]
x = df[["Ice cream sales"]]

"""
Use an algorithm to fit the training data to a model, in the case of a regression model, use regression aorithm such as linear regression
"""
modelo.fit(
    x.values, y.values)  # using .values to get the data from the column of each df

print(modelo.predict([[4]])[0][0])  # predict() as default, and  twice [[]]
