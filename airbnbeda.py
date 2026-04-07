import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('datasets.csv')
# print(data.head())
# data.tail()
# data.info()

data["baths"] = data["baths"].replace("Not specified",np.nan)
print(data.head())
data["baths"] = data["baths"].astype(float)
data["bedrooms"] = data["bedrooms"].replace("Studio",np.nan)
data["bedrooms"] = data["bedrooms"].astype(float)
# data.info()
# print(data.head(20))
# print(data.describe())

# In "bedrooms" column approx 8% of the data is missing and in "others" column approx 0.5% of the data is missing.
# We can fill the rows with missing values in "bedrooms" columnwith the median value, and fill the missing values in "baths" column with'meanormode' value of that column.

data["bedrooms"]=data["bedrooms"].fillna(data["bedrooms"].median())
data["baths"]=data["baths"].fillna(data["baths"].mean())
data["neighbourhood"]=data["neighbourhood"].fillna(data["neighbourhood"].mode()[0])

data.info()
print(data.head(10))
print(data.isnull().sum().sum())
data.dropna(inplace=True)
print(data.isnull().sum().sum())
data.drop_duplicates(inplace=True)
print(data.duplicated().sum())
data.info()

data['id'] = data['id'].astype(object)
data['host_id'] = data['host_id'].astype(object)


#Price distribuion
plt.figure(figsize=(6, 3))
sns.histplot(data=data, x='availability_365')
plt.title('availability_365 Distribuition')
plt.ylabel("Frequency")
plt.show()



grpbyprice=data.groupby('neighbourhood_group')['price'].mean()
print(grpbyprice)

# ['price per bed']

data['price_per_bed']= data['price']/data['beds']
print(data.head())

grpbypricebed=data.groupby('neighbourhood_group')['price_per_bed'].mean()
print(grpbypricebed)

print(data.columns)

plt.bar('neighbourhood_group','price',data=data)
plt.show()


plt.figure(figsize=(8, 5))
plt.title("Locality and Review Dependency")
plt.scatter(data=data,x='number_of_reviews',y='price')
plt.show()

df = data[data['price'] < 1500]

plt.figure(figsize=(8, 5))
plt.title("Locality and Review Dependency")
plt.scatter(data=df, x='number_of_reviews', y='price',color="pink")
plt.show()

plt.figure(figsize=(8,5))
grpbyprice.sort_values().plot(kind='bar')

plt.title("Average Price by Neighbourhood Group")
plt.xlabel("Neighbourhood Group")
plt.ylabel("Average Price")

plt.show()


'''

>>>>
Some neighbourhood groups have significantly higher average prices. 
These areas likely represent premium locations with higher demand or better amenities. 
Lower-priced neighbourhoods indicate budget-friendly or less popular areas.
“This insight is derived from grouping listings by neighbourhood and comparing their average prices.”


>>>>>>Reviews vs Price Relationship
Listings with a higher number of reviews are generally in the lower to mid-price range.
Expensive listings tend to have fewer reviews, indicating lower booking frequency.

>>>>>Insight from availability_365 Distribution

Listings with low availability are highly popular and get booked often.
A large number of listings are not getting enough bookings and remain available throughout the year.
Most listings fall into extreme categories (very high or very low demand) rather than moderate demand.

>>>>Insight from Neighbourhood Distribution
Brooklyn dominates the Airbnb market in terms of listing count, indicating high supply and competition.
Staten Island shows minimal participation, indicating low demand and market activity

>>>>Impact of Outliers
High-priced listings (above 1500) act as outliers and distort the analysis.
Removing these outliers provides a clearer and more realistic understanding of pricing trends.
'''


