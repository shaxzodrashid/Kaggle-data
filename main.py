# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Airbnb dataset
df = pd.read_csv('AB_NYC_2019.csv')

# Display the first few rows to understand the data
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Handle missing values
# For simplicity, we will fill the missing 'reviews_per_month' with 0
df['reviews_per_month'].fillna(0, inplace=True)

# Drop rows with missing 'name' and 'host_name' as they are less critical
df.dropna(subset=['name', 'host_name'], inplace=True)

# Convert 'last_review' to datetime format
df['last_review'] = pd.to_datetime(df['last_review'])

# Verify data types
print(df.dtypes)

# Data Analysis

# 1. Most Expensive Neighbourhood Groups (Boroughs)
# Calculate average price per neighbourhood group
price_by_neighbourhood_group = df.groupby('neighbourhood_group')['price'].mean().reset_index()
print(price_by_neighbourhood_group)

# Visualize average price by neighbourhood group
plt.figure(figsize=(10,6))
sns.barplot(x='neighbourhood_group', y='price', data=price_by_neighbourhood_group)
plt.title('Average Price by Neighbourhood Group')
plt.ylabel('Average Price')
plt.xlabel('Neighbourhood Group')
plt.show()

# 2. Price by Room Type
# Calculate average price per room type
price_by_room_type = df.groupby('room_type')['price'].mean().reset_index()
print(price_by_room_type)

# Visualize average price by room type
plt.figure(figsize=(10,6))
sns.barplot(x='room_type', y='price', data=price_by_room_type)
plt.title('Average Price by Room Type')
plt.ylabel('Average Price')
plt.xlabel('Room Type')
plt.show()

# 3. Reviews and Ratings Analysis
# Since 'reviews' and 'ratings' columns are not directly available, we will use 'number_of_reviews' and 'reviews_per_month'
# Analyze the relationship between number of reviews and price
plt.figure(figsize=(10,6))
sns.scatterplot(x='number_of_reviews', y='price', data=df)
plt.title('Number of Reviews vs Price')
plt.ylabel('Price')
plt.xlabel('Number of Reviews')
plt.show()

# Analyze the relationship between reviews per month and price
plt.figure(figsize=(10,6))
sns.scatterplot(x='reviews_per_month', y='price', data=df)
plt.title('Reviews per Month vs Price')
plt.ylabel('Price')
plt.xlabel('Reviews per Month')
plt.show()

# Correlation Analysis
correlation = df[['price', 'number_of_reviews', 'reviews_per_month']].corr()
print(correlation)

# Visualize the correlation matrix
plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True)
plt.title('Correlation Matrix')
plt.show()

'''Conclusion:
1. Most expensive neighbourhood groups can be identified from the bar plot.
2. Price varies significantly with room type.
3. Number of reviews and reviews per month have a weak correlation with price.'''