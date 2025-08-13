import pandas as pd

df = pd.read_csv('bestsellers.csv')

print(df.describe())

df.drop_duplicates(inplace=True)

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

df["Price"] = df["Price"].astype(float)

print(df.describe())
