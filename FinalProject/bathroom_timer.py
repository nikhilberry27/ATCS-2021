"""
@author: Nikhil Berry
@version: 05/10/2022
Program App Name: Nature's Calling
"""

# Import necessary libraries
import pandas as pd
import csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class bathroomTimePredictor:
    # Constructor
    def __init__(self):
        self.user_name = None
        self.csv_name = None
        self.user_data = None
        self.scaler = None
        self.model = None

    # Access user account (stored CSV) or create a new one
    # Ensure there is adequate baseline data or add more
    def access_user_account(self):
        #prompt user to access their account (stored CSV)
        self.user_name = input("What is your name? ")
        self.csv_name = "bathroom_" + self.user_name + ".csv"
        no_file = False

        #try to access account but if none exists then create a new one
        try:
            self.user_data = pd.read_csv(self.csv_name)
            print("Accessing existing user account now.")
        except FileNotFoundError:
            print("Creating new user account now.")
            self.user_data = []
            no_file = True

        #confirm there is adequate baseline data (20 datapoints)
        if len(self.user_data) < 21:
            with open(self.csv_name, 'a') as f:
                w = csv.writer(f, quoting=csv.QUOTE_NONE)

                #add baseline data if there is not adequate data
                if no_file:
                    w.writerow(["age", "weight", "given_birth", "water_consumption", "time_to_next_bathroom"])
                for i in range(20-len(self.user_data)):
                    #assuming that user will enter data in correct format as prompted
                    print("Adding baseline data.")
                    age = input("How old are you? ")
                    weight = input("How much do you weigh? (lbs): ")
                    given_birth = input("Have you given birth? (0-n,1-y): ")
                    water_consumption = input("How much water have you consumed since your last bathroom visit? (ml): ")
                    time_to_next_bathroom = input("What time did you have to use the bathroom next? (mins): ")
                    w.writerow([age, weight, given_birth, water_consumption, time_to_next_bathroom])

    # Run regression model
    def run_model(self):
        #load Data
        data = pd.read_csv(self.csv_name)
        x_1 = data["age"]
        x_2 = data["weight"]
        x_3 = data["given_birth"]
        x_4 = data["water_consumption"]
        y = data["time_to_next_bathroom"]
        #print(data)

        #reload and/or reformat the data to get the values from x and y
        x = data[["age", "weight", "given_birth", "water_consumption"]].values
        y = data["time_to_next_bathroom"].values

        #scale the model
        #print(x)
        self.scaler = StandardScaler().fit(x)
        x = self.scaler.transform(x)

        #separate data into training and test sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        #create multivariable linear regression model
        self.model = LinearRegression().fit(x_train, y_train)

        # Find and print the coefficients, intercept, and r squared values.
        # Each rounded to two decimal places.
        #print("Model Information")
        # print("Age coef: ", round(float(model.coef_[0]), 2))
        # print("Weight coef: ", round(float(model.coef_[1]), 2))
        # print("Given_birth coef: ", round(float(model.coef_[2]), 2))
        # print("Water consumption coef: ", round(float(model.coef_[3]), 2))
        # print("Intercept: ", round(float(model.intercept_), 2))
        # print("R-squared: ", round(float(model.score(x_train,y_train)), 2))
        # print()

        #test the model
        predictions = self.model.predict(x_test)

        #print out the actual vs the predicted values
        #print("Testing Linear Model with Test Data:")
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
            #print("Age:", x_age, "Weight:", x_weight, "Given Birth:", x_given_birth, "Water Consumption: ", x_water_consumption, "Predicted Time:", y_pred, "Actual Time:", actual)

    # Make a new prediction based on baseline data
    def make_new_prediction(self):
        #collect input data for prediciton
        #assuming that user will enter data in correct format as prompted
        print("You will be receiving a prediction based on the following input data now.")
        age_pred = input("How old are you? ")
        weight_pred = input("How much do you weigh? (lbs): ")
        given_birth_pred = input("Have you given birth? (0-n,1-y): ")
        water_consumption_pred = input("How much water have you consumed since your last bathroom visit? (ml): ")

        #scale the inputs
        x_pred = [[age_pred, weight_pred, given_birth_pred, water_consumption_pred]]
        x_pred = self.scaler.transform(x_pred)

        #make the prediction
        prediction = self.model.predict(x_pred)
        prediction_val = prediction[0]

        #print the prediction
        print("The predicted time you will have to use the bathroom next is in ", prediction_val, " minutes.")

# Main Method
if __name__ == '__main__':
    predictor = bathroomTimePredictor()
    predictor.access_user_account()
    predictor.run_model()
    predictor.make_new_prediction()