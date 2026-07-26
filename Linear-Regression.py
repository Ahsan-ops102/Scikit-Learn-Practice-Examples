from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [40,50,65,75,90]

model = LinearRegression()
model.fit(X, y)

hours = float(input("Enter the number of study hours: "))
predicted_score = model.predict([[hours]])

print(f"Predicted test score for {hours} study hours is: {predicted_score[0]}")