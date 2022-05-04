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
from sklearn.preprocessing import StandardScaler


user_name = input("What is your name?")
csv_name = "bathroom_" + user_name + ".csv"

no_file = False
try:
    user_data = pd.read_csv(csv_name)
    print("Accessing existing user account now.")
except FileNotFoundError:
    print("Creating new user account now.")
    user_data = []
    no_file = True



# Collect user-inputted data
#user_data = pd.read_csv("bathroom_user.csv")
if len(user_data) < 5:
    with open(csv_name, 'a') as f:
        w = csv.writer(f, quoting=csv.QUOTE_NONE)

        if no_file:
            w.writerow(["age", "weight", "given_birth", "water_consumption", "time_to_next_bathroom"])
        for i in range(21-len(user_data)):
            age = input("How old are you? ")
            weight = input("How much do you weigh? (lbs): ")
            given_birth = input("Have you given birth? (0-n,1-y): ")
            water_consumption = input("How much water have you consumed since your last bathroom visit? (ml): ")
            time_to_next_bathroom = input("What time did you have to use the bathroom next?: ")
            w.writerow([age, weight, given_birth, water_consumption, time_to_next_bathroom])


# Load Data
data = pd.read_csv(csv_name)
x_1 = data["age"]
x_2 = data["weight"]
x_3 = data["given_birth"]
x_4 = data["water_consumption"]
y = data["time_to_next_bathroom"]

print(data)
''' TODO: Create Linear Regression '''

# Reload and/or reformat the data to get the values from x and y
x = data[["age", "weight", "given_birth", "water_consumption"]].values
y = data["time_to_next_bathroom"].values

#Scale the model
print(x)
scaler = StandardScaler().fit(x)
x = scaler.transform(x)


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
print("Water consumption coef: ", round(float(model.coef_[3]), 2))


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
    x_water_consumption = x_test[index][3]
    print("Age:", x_age, "Weight:", x_weight, "Given Birth:", x_given_birth, "Water Consumption: ", x_water_consumption, "Predicted Time:", y_pred, "Actual Time:", actual)

# Make a new prediction
age_pred = input("How old are you? ")
weight_pred = input("How much do you weigh? (lbs): ")
given_birth_pred = input("Have you given birth? (0-n,1-y): ")
water_consumption_pred = input("How much water have you consumed since your last bathroom visit? (ml): ")

# Scale the inputs
x_pred = [[age_pred, weight_pred, given_birth_pred, water_consumption_pred]]
x_pred = scaler.transform(x_pred)

# Make and print the prediciton
prediction = model.predict(x_pred)
print(prediction)

#print("The predicted time you will have to use the bathroom next is in " + prediction + " minutes.")



#im yours

#tkinter


