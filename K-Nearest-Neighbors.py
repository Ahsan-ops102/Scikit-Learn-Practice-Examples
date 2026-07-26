from sklearn.neighbors import KNeighborsClassifier

# Features: [weight, size]
# 0 = Apple, 1 = Orange
X = [
    [180, 7],
    [200, 7.5],
    [250, 8],
    [300, 8.5],
    [330, 9],
    [360, 9.5]
]

y = [0, 0, 0, 1, 1, 1]


model = KNeighborsClassifier(n_neighbors=3)

model.fit(X,y)

weight = float(input("Enter the weight of the fruit: "))
size = float(input("Enter the size of the fruit: "))
predicted_fruit = model.predict([[weight, size]])[0]

if predicted_fruit == 0:
    print(f"The fruit with weight {weight} and size {size} is predicted to be an Apple.")
else:
    print(f"The fruit with weight {weight} and size {size} is predicted to be an Orange.")
