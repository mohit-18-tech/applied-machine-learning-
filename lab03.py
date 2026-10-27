import pandas as pd
import numpy as np
# These are the headers which you need to link to your dataset.
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv('car_dataset.data', names = headers)
# To see what the data set looks like, we'll use the head() method.
df.head(10)
# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)
missing_data = df.isnull()
missing_data.head(5)
for column in headers:
    print(column)
    print (missing_data[column].value_counts())
    print("")  
avg_norm_loss = df["normalized-losses"].astype('float').mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)

df["normalized-losses"].replace(np.nan, avg_norm_loss,inplace = True)
avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)

df["bore"].replace(np.nan, avg_bore,inplace = True)

avg_bore=df['stroke'].astype('float').mean(axis=0)
print("Average of stroke:", avg_bore)

df["stroke"].replace(np.nan, avg_bore, inplace=True)
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)

df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)

df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

df['num-of-doors'].value_counts()

df['num-of-doors'].value_counts().idxmax()
#replace the missing 'num-of-doors' values by the most frequent 
df["num-of-doors"].replace(np.nan, "four", inplace=True)
# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)
missing_data = df.isnull()
missing_data.head(5)

for column in headers:
    print(column)
    print (missing_data[column].value_counts())
    print("") 

df.info()      
#You can check it by exporting the correct dataset and then reload it again in dataframe as I have shown in tutorial.
df1 = pd.read_csv('no_null.csv')
df1.info()

#Convert ["bore", "stroke","peak-rpm","price","normalized-losses", "horsepower"] data types to float data types.
df[["bore", "stroke","peak-rpm","price","normalized-losses", "horsepower"]] = df[["bore", "stroke","peak-rpm","price","normalized-losses", "horsepower"]].astype(float)

#Check it with info method.
df.info()

#Lets first change the data type of horsepower because I forgot to include it in to_float list of upper cell.
df['horsepower'].astype(float)

# lets visualize the horsepower data in histogram
import matplotlib.pyplot as plt
plt.hist(df['horsepower'])
plt.xlabel('HorsePower')
plt.ylabel('Count')
# Create bins.
bins = np.linspace(min(df['horsepower']), max(df['horsepower']), 4)
bins
# Create group names.
group_names = ["Low", "Medium", "High"]
# perform binning.
df['horsepower-bins'] = pd.cut(df['horsepower'], bins, include_lowest=True, labels=group_names)
# See the frequency of each bin with value_counts()
df['horsepower-bins'].value_counts()
# Lets visualize again with bins.
plt.bar(group_names, df['horsepower-bins'].value_counts())
plt.xlabel("HorsePower Capacity")
plt.ylabel("Total Count")
