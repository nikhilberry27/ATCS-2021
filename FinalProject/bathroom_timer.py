"""
@author: Nikhil Berry
@version: 04/28/2022
Current App Name: Nature Called
"""

import pandas as pd
import matplotlib.pyplot as plt
import csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Collect user-inputted data
with open('bathroom_user.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_NONE)

    w.writerow(["age", "weight", "given_birth", "water_consumption", "time_to_next_bathroom"])
    for i in range(2):
        age = input("How old are you? ")
        weight = input("How much do you weigh? (lbs): ")
        given_birth = input("Have you given birth? (0-n,1-y): ")
        water_consumption = input("How much water have you consumed since your last bathroom visit? (ml): ")
        time_to_next_bathroom = input("What time did you have to use the bathroom next?: ")
        w.writerow([age, weight, given_birth, water_consumption, time_to_next_bathroom])


''' Load Data '''
data = pd.read_csv("bathroom_user.csv")
x_1 = data["age"]
x_2 = data["weight"]
x_3 = data["given_birth"]
y = data["time_to_next_bathroom"]

''' TODO: Create Linear Regression '''
# Reload and/or reformat the data to get the values from x and y
x = data[["age", "weight", "given_birth"]].values
y = data["time_to_next_bathroom"].values

# Separate data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Create multivariable linear regression model
model = LinearRegression().fit(x_train, y_train)

# Find and print the coefficients, intercept, and r squared values.
# Each rounded to two decimal places.
print("Model Information")
print("Age coef: ", round(float(model.coef_[0]), 2))
print("Weight coef: ", round(float(model.coef_[1]), 2))
print("Given_birth coef: ", round(float(model.coef_[2]), 2))

print("Intercept: ", round(float(model.intercept_), 2))
print("R-squared: ", round(float(model.score(x_train,y_train)), 2))
print()

# Test the model
predictions = model.predict(x_test)

# Print out the actual vs the predicted values
print("Testing Linear Model with Test Data:")
for index in range(len(x_test)):
    #Actual y value
    actual = y_test[index]

    # Predicted y value
    y_pred = predictions[index]

    # Test x values
    x_age = x_test[index][0]
    x_weight = x_test[index][1]
    x_given_birth = x_test[index][2]
    print("Age:", x_age, "Weight:", x_weight, "Given Birth:", x_given_birth, "Predicted Time:", y_pred, "Actual Time:", actual)


