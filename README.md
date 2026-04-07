<p align="center">
  <img src="images/banner.jpg" width="100%">
</p>

# Airbnb Data Analysis (EDA)

## Overview
...
# Airbnb Data Analysis (EDA)

## 📊 Overview
This project focuses on cleaning and analyzing Airbnb listing data to understand pricing patterns, demand trends, and customer behavior across different neighbourhoods.

---

## 🧹 Data Cleaning
- Handled missing values in key columns:
  - Bedrooms → filled with median  
  - Baths → filled with mean  
  - Neighbourhood → filled with mode  
- Converted data types for consistency  
- Removed remaining null values  
- Dropped duplicate records  

---

## ⚙️ Feature Engineering
- Created a new feature:  
  **price_per_bed = price / beds**

---

## 📈 Analysis & Visualizations
- Distribution of availability (`availability_365`)  
- Price comparison across neighbourhood groups  
- Relationship between number of reviews and price  
- Outlier handling for better analysis  

---

## 🔍 Key Insights
- Affordable listings receive more reviews and bookings  
- Expensive listings have lower engagement  
- Demand is concentrated in lower to mid-price range  
- Some neighbourhoods are significantly more expensive than others  
- Many listings remain available for most of the year, indicating low demand  

---

## 🛠️ Tools Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  


---

## 📁 Files
- `airbnbeda.py` → main analysis script  
- `datasets.csv` → dataset  
- Images → visualizations  

---

## 🚀 Conclusion
This project demonstrates end-to-end data analysis, including data cleaning, feature engineering, and extracting meaningful insights from real-world data.

---

## 👤 Author
Chitransh Jain
