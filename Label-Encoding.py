import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("sample_label_encoding_data.csv")
df_label = df.copy()

le = LabelEncoder()
df_label['Gender Encoded'] = le.fit_transform(df_label['gender'])
df_label['City Encoded'] = le.fit_transform(df_label['city'])

encoded_df = pd.get_dummies(df, columns=['city'],dtype = int)

print("\n Encoded DataFrame:")
print(df_label[['gender','Gender Encoded']].head(5))  

print("\n One-Hot Encoded DataFrame:")
print(encoded_df.head(5))