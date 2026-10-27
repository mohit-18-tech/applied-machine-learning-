#dealing with categorical values 
import pandas as pd
import numpy as np

df = pd.read_csv("Salary_Dataset.csv")
df.head(40)
# Get dummies with pandas in any variable
country_dummy = pd.get_dummies(df['country']).astype(int)
country_dummy

# concatenate the dataframes into original dataframes.
df = pd.concat([df, country_dummy], axis=1)

# Drop the country column and rearrange the index of column.
df.drop('country', axis=1, inplace=True)
df = df[['Australia', 'Canada', 'Dubai', 'USA', 'Salary', 'YearsExperience', 'Purchased']]

print(df.head(40))
