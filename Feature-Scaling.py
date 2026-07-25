import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split

data = {
    'Study hours': [1,2,3,4,5],
    'Test scores': [40,50,60,70,80]
}

df = pd.DataFrame(data)

standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(df)

print("\n Standard Scaled DataFrame:")
print(pd.DataFrame(standard_scaled, columns = ['Study hours','Test scores']))

print("\n")

minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df)

print("\n Min-Max Scaled DataFrame:")
print(pd.DataFrame(minmax_scaled, columns = ['Study hours','Test scores']))

print("\n")

X = df[['Study hours']]
y = df[['Test scores']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state =42)

print("\n Training Data:")
print(X_train)

print("\n Testing Data:")
print(X_test)