# Data Analysis: Software Professional Salaries

## Overview
This project analyzes a dataset of over 20,000 software professionals, focusing on various aspects such as salaries, job roles, company ratings, and locations. The analysis is performed using Python, with an emphasis on data manipulation, visualization, and API integration.

## Dataset
The dataset, "Software Professionals Salary.csv", contains information about software professionals, including:
- Company Rating
- Company Name
- Job Title
- Salary (in Indian Rupee ₹)
- Number of Salaries Reported
- Company Location
- Employment Status
- Job Role Category

Source: [Kaggle - Software Professional Salaries 2022](https://www.kaggle.com/datasets/iamsouravbanerjee/software-professional-salaries-2022?search=salary)

## Technologies Used
- Python
- Pandas for data manipulation
- Matplotlib and Seaborn for data visualization
- Requests library for API integration

## Key Features
1. Data loading and initial exploration
2. Analysis of unique job roles and titles
3. Company-specific analyses
4. Currency conversion using ExchangeRate-API
5. Salary analysis across different job roles and companies
6. Visualization of salary vs company rating relationship

## Main Findings
- The dataset contains 22,770 entries with 8 columns
- There are 11 unique job roles in the dataset
- Amazon has the highest number of salary reports across all job titles
- A real-time currency conversion from INR to USD was implemented
- Identified the company with the highest average salary in USD
- Created a scatter plot showing the relationship between average salary and company rating, revealing some interesting outliers

## Visualizations
The project includes a scatter plot that visualizes the relationship between average salaries and company ratings, highlighting potential anomalies in the data.

