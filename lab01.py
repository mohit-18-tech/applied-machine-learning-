import numpy as np
import pandas as pd
headers_data = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", type(headers_data))
df = pd.read_csv('dataset_1.data', names=headers_data)
df.head()
df.tail()
df.dtypes
df.describe()
df.describe(include="all")# describe all the columns in "df" 
#Replacing "?" with np.nan so that pandas can recognize the null values.
df.replace("?", np.nan, inplace=True)
# look at the info of "df"
df.info()
df.to_csv('Done_with_Practice.data', index=False)


