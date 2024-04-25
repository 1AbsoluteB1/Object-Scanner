# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Create a sample dataset with two independent variables (X1 and X2) and one dependent variable (Y)
# Replace this with the actual dataset you intend to use
# For this example, let's CSV file named "dataset.csv"

# Load the dataset
def Linear():
    dataset = pd.read_excel('Book1.xlsx', sheet_name='Sheet1')

    # Define the independent variables (X) and the dependent variableY)
    X = dataset[['Height Difference', 'Pixel Length']]
    Y = dataset['Length']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Create the linear regression model
    model = LinearRegression()

    # Train the model using the training sets
    model.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = model.predict(X_test)

    # Model evaluation
    print('Coefficients:', model.coef_)
    print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
    print('Coefficient of Determination (R^2):', r2_score(y_test, y_pred))
Linear()
def Line():
    import numpy as np
    from sklearn.linear_model import LinearRegression

    dataset = pd.read_excel('Book1.xlsx', sheet_name='Sheet1')

    # Define the independent variables (X) and the dependent variableY)
    X = dataset[['Height Difference', 'Pixel Length']]
    Y = dataset['Length']
    # Create a linear regression model
    model = LinearRegression()

    # Fit the model with the data
    model.fit(X, Y)

    # Get the coefficients and intercept
    coefficients = model.coef_
    intercept = model.intercept_

    # Print Linear Equation
    print("Linear Equation:")
    print(f"y = {coefficients[0]} * x1 + {coefficients[1]} * x2 + {intercept}")
    return coefficients, intercept
Line()
