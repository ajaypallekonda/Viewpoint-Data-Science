import pandas as pd

# Problem 2 part 1
# Move into a pandas dataframe
df1 = pd.read_csv("2017.csv")

# Drops all rows or columns which only have NaN values
df1.dropna(how ="all")
print(df1)

# Problem 2 part 2
df2 = pd.read_csv("data.csv")
df2.columns = ['Index', 'Value']

print(df2['Value'].describe())