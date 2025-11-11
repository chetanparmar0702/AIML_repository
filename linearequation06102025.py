import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


data = {
    'Experience': [1, 2, 3, 4, 5, 6],
    'Salary': [35000, 40000, 45000, 50000, 55000, 60000]
}
df = pd.DataFrame(data)

# Step 3: Split into X and y
X = df[['Experience']]
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


model = LinearRegression()
model.fit(X_train, y_train)


predictions = model.predict(X_test)


error = mean_squared_error(y_test, predictions, squared=False)
print(f"Predicted values: {predictions}")
print(f"RMSE Error: {error:.2f}")