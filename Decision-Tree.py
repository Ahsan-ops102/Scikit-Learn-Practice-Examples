from sklearn.tree import DecisionTreeClassifier

# Features: [color, weight]
# 0 = Apple, 1 = Orange
X = [
    [7, 2],      # Apple
    [8, 3],      # Apple
    [9, 8],      # Orange
    [10, 9]      # Orange
]

y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

color = float(input("Enter the color of the fruit (1-10): "))
weight = float(input("Enter the weight of the fruit (1-10): "))
predicted_fruit = model.predict([[color, weight]])[0]

if predicted_fruit == 0:
    print(f"The fruit with color {color} and weight {weight} is predicted to be an Apple.")
else:
    print(f"The fruit with color {color} and weight {weight} is predicted to be an Orange.")