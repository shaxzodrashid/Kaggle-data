# Airbnb NYC Data Analysis

## Overview

This project analyzes the Airbnb listings data from New York City. Using Python libraries such as `pandas`, `matplotlib`, and `seaborn`, we explore different aspects of the data, including the relationship between price, location, room type, and reviews. The analysis aims to uncover trends and patterns in the listings that can help potential customers and hosts understand the dynamics of the Airbnb market in NYC.

## Dataset

The dataset used in this analysis is the Airbnb listings for New York City from 2019. It contains various features about the properties listed on Airbnb, such as:

- `id`: Unique identifier for the listing
- `name`: Name of the Airbnb listing
- `host_id`: Unique identifier for the host
- `neighbourhood_group`: The broader area of NYC where the listing is located (e.g., Manhattan, Brooklyn)
- `neighbourhood`: The specific neighborhood of the listing
- `latitude` & `longitude`: Location coordinates
- `room_type`: Type of the room (Entire home, private room, etc.)
- `price`: Price per night for the listing
- `minimum_nights`: Minimum number of nights required to stay
- `number_of_reviews`: Number of reviews the listing has received
- `last_review`: Date of the most recent review
- `reviews_per_month`: Average number of reviews per month
- `calculated_host_listings_count`: Number of listings the host has
- `availability_365`: Number of days the listing is available in a year

## Libraries Used

- **Pandas**: For data manipulation and cleaning.
- **Matplotlib**: For data visualization.
- **Seaborn**: For advanced visualizations and aesthetics.
- **Numpy**: For numerical computations.

## Data Cleaning

Before analyzing the data, the following cleaning steps were taken:

1. **Handling Missing Data**:
   - Missing values in the `reviews_per_month` column were filled with 0, as they represent listings without any reviews.
   - Rows missing `name` and `host_name` were dropped, as they were deemed less critical to the analysis.

2. **Date Formatting**:
   - The `last_review` column was converted to a datetime format to ensure consistency when working with review dates.

## Analysis

### 1. Most Expensive Neighbourhood Groups

We calculated the average price per night for each neighborhood group (borough) and visualized the results using a bar chart. This analysis helps identify which boroughs have the most expensive listings on average.

### 2. Room Type and Price Analysis

We explored how the price varies depending on the room type. This analysis categorizes listings into entire homes, private rooms, shared rooms, etc., and compares their average prices.

### 3. Reviews Analysis

Using the `number_of_reviews` and `reviews_per_month` columns, we investigated the relationship between the number of reviews and the price of the listing. We created scatter plots to see if there was a pattern between how many reviews a listing has and its nightly price.

### 4. Correlation Analysis

We performed a correlation analysis between the price, number of reviews, and reviews per month. The correlation matrix was visualized using a heatmap to better understand any potential relationships between these variables.

## Key Insights

1. **Neighbourhood Groups**:
   - The most expensive neighbourhood groups (boroughs) are identified, showing where customers can expect to pay the highest prices in NYC.
   
2. **Room Types**:
   - Entire homes tend to have significantly higher prices compared to private and shared rooms.
   
3. **Reviews**:
   - There is a weak correlation between the number of reviews or reviews per month and the price of the listing. This suggests that other factors, such as location or room type, might have a stronger influence on price.
   
## How to Run the Code

To run this project, make sure you have Python installed along with the following libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

After installing the necessary libraries, you can run the script in any Python environment by downloading the dataset and executing the script provided in this repository.

**Conclusion**
This analysis provides a clear overview of the dynamics of the Airbnb market in New York City. By understanding which areas and room types command higher prices, and seeing the relationship between reviews and price, hosts and customers can make more informed decisions.

**Future Improvements**
### Perform more detailed spatial analysis using latitude and longitude to visualize listings on a map.
### Incorporate machine learning models to predict prices based on available features.
