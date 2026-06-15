# E-Commerce Sales Data Analysis and Visualization

## Project Overview

This project focuses on cleaning, analyzing, and visualizing e-commerce sales data using Python. The objective is to extract meaningful insights from customer transactions, identify sales trends, detect outliers, and create visual reports for better business decision-making.

## Features

### Data Cleaning

* Detect and handle missing values
* Replace missing coupon codes with default values
* Remove duplicate records
* Convert date columns into datetime format
* Convert numerical columns into appropriate data types
* Clean text data by removing unnecessary spaces

### Data Analysis

* Calculate:

  * Mean
  * Median
  * Mode
  * Count
* Product-wise sales analysis
* Product popularity analysis
* Revenue analysis
* Payment method analysis

### Outlier Detection

* Uses the Interquartile Range (IQR) method
* Identifies unusual transaction values
* Displays total number of outliers

### Data Visualization

* Bar Charts
* Pie Charts
* Product Popularity Charts
* Revenue Analysis Graphs
* Payment Method Distribution Charts

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Microsoft Excel

## Project Structure

```text
Project/
│
├── Cleaned_Dataset.xlsx
├── project.py          # Data Cleaning
├── project2.py         # Data Analysis & Visualization
├── project4.py         # Advanced Visualizations
├── README.md
```


## Running the Project

### Step 1: Data Cleaning

```bash
python project.py
```

This script:

* Removes duplicates
* Handles missing values
* Converts data types
* Creates a cleaned dataset

### Step 2: Data Analysis

```bash
python project2.py
```

This script:

* Performs descriptive statistics
* Detects outliers
* Generates sales visualizations

### Step 3: Advanced Visualizations

```bash
python project4.py
```

This script:

* Shows top products by revenue
* Displays referral source distribution
* Analyzes payment method usage

## Sample Insights

* Which products generate the highest revenue
* Most popular products among customers
* Preferred payment methods
* Referral sources driving the most sales
* Detection of unusually large transactions

## Learning Outcomes

Through this project, the following skills were developed:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Visualization
* Statistical Analysis
* Business Insight Generation
* Python Programming

## Author

Abhi Shah


