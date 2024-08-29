# Data Analysis: Software Professional Salaries

## Overview
This project analyzes a dataset of over 20,000 software professionals. It focuses on salaries, job roles, company ratings, and locations using Python for data manipulation, visualization, and API integration.

## Dataset
The dataset, "Software Professionals Salary.csv", includes:
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
- Pandas (data manipulation)
- Matplotlib and Seaborn (visualization)
- Requests (API integration)

## Key Features
1. Data loading and initial exploration
2. Analysis of job roles and titles
3. Company-specific insights
4. Currency conversion from INR to USD using ExchangeRate-API
5. Salary analysis across job roles and companies
6. Visualization of salary vs company rating

## Main Findings
- The dataset has 22,770 entries with 8 columns
- There are 11 unique job roles
- Amazon has the highest number of salary reports
- Real-time currency conversion from INR to USD was used
- Identified the company with the highest average salary in USD
- Scatter plot reveals the relationship between average salary and company rating, highlighting interesting outliers

## Visualizations
The project includes a scatter plot showing the relationship between average salary and company rating, with notable data anomalies.

## Calculations
All calculations and analyses were performed in the file [software-salaries-analysis.py](/software-salaries-analysis.py).
