import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: set a clean style for plots
sns.set_theme(style="whitegrid")

# Load data
df = pd.read_csv("bestsellers.csv")  # replace with your dataset

plt.figure(figsize=(8, 5))
sns.histplot(df['Price'], bins=20, kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Price ($)")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6, 5))
sns.boxplot(x=df['User Rating'])
plt.title("Distribution of User Ratings")
plt.xlabel("User Rating")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x="Genre", y="Price", data=df)
plt.title("Book Price Distribution by Genre")
plt.show()
