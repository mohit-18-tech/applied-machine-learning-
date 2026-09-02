import numpy as np
import pandas as pd
# These are the headers which you need to link to your dataset.
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df=pd.read_csv('car_dataset.data', names=headers)
# To see what the data set looks like, we'll use the head() method.
df.head()
df.replace("?",np.nan,inplace=True)
missing = df.isnull()
# count missing values in each column
for column in headers:
    print(missing[column].value_counts())
    print(" ")
normalize_avg = df["normalized-losses"].astype('float').mean()
normalize_avg 
df['normalized-losses'].replace(np.nan, normalize_avg, inplace=True)
df['normalized-losses'] 
bore_mean=df['bore'].astype('float').mean()
df['bore'].replace(np.nan,bore_mean,inplace=True)
stroke_mean=df['stroke'].astype('float').mean()
df['stroke'].replace(np.nan,stroke_mean,inplace = True)
df['stroke'].info()
hp_avg = df['horsepower'].astype('float').mean()
hp_avg
rpm_avg = df['peak-rpm'].astype("float").mean()
rpm_avg
df['peak-rpm'].replace(np.nan, rpm_avg, inplace = True)
df['peak-rpm']
# Find the most frequent value for num of doors
df['num-of-doors'].value_counts()
df['num-of-doors'].value_counts().idxmax()
#replace the missing 'num-of-doors' values by the most frequent 
df['num-of-doors'].replace(np.nan, df['num-of-doors'].value_counts().idxmax(), inplace=True)
# simply drop whole row with NaN in "price" column
df.dropna(subset = ['price'], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)
missing_data = df.isnull()
for column in headers:
    print(missing_data[column].value_counts())
    print(" ")
df.info()    

