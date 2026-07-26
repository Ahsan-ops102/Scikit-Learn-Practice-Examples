from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5]]
y = [0,0,0,1,1]

model = LogisticRegression()

model.fit(X,y)

hours = float(input("Enter the number of study hours: "))
predicted_result = model.predict([[hours]])[0]

if predicted_result == 1:
    print(f"Predicted result for {hours} study hours is: Pass")
else:
    print(f"Predicted result for {hours} study hours is: Fail")