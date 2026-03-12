import pandas as pd

# %%
# reading the database
data = pd.read_csv("tips.csv")

# %%
# printing the top 10 rows
print(data.head(10))

# %%
# Info dataset
print("\nInfo Dataset:")
print(data.info())

# %%
# Statistik deskriptif
print("\nStatistik Deskriptif:")
print(data.describe())
