# Setup and Data Loading
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# Load the dataset
sps = pd.read_csv('Software Professionals Salary.csv')

# Print column datatypes
print(sps.dtypes)

# Display the first few rows
sps.head()

# Objective 1: Determine the structure of the `sps` DataFrame in terms of rows and columns.
print(sps.shape)

# Objective 2: Identify the number of unique roles in the `Job Roles` column and list them.
print(sps['Job Roles'].nunique())
print(sps['Job Roles'].unique())

# Objective 3: Calculate the number of unique `Job Titles` associated with the `Python` role.
python_role = sps[sps['Job Roles'] == 'Python']
upjt = python_role['Job Title'].nunique()
print("Number of unique Python roles in Job Titles:", upjt)

# Objective 4: Find out how many companies offer a `Python` role with a `Job Title` containing the word "Analyst".
par = sps[(sps['Job Roles'] == 'Python') & sps['Job Title'].str.contains('Analyst', case=False)]
ucpa = par['Company Name'].nunique()
print('Companies with a Python Job Role and a Job Title containing the word "Analyst":', ucpa)

# Objective 5: Identify the `Company Name` with the highest number of `Salaries Reported` across all `Job Titles`.
ssc = sps.groupby('Company Name')['Salaries Reported'].sum()
cms = ssc.idxmax()
ms = ssc.max()
print(f"The Company with the highest number of Salaries Reported is '{cms}' with a total of {ms} reports.")

# Objective 6: Determine how many `Location`s the company identified in the previous step is present in.
csl = sps[sps['Company Name'] == 'Amazon']
ulc = csl['Location'].nunique()
print(f"The company Amazon is present in {ulc} locations.")

# Objective 7: Create a new column `Salary USD` that contains the salary equivalent in USD.
def get_inr_to_usd_rate():
    url = "https://open.er-api.com/v6/latest/INR"
    r = requests.get(url)
    data = r.json()
    if r.status_code == 200:
        return data['rates']['USD']
    else:
        return "Conversion rate unavailable!"

itur = get_inr_to_usd_rate()
print(f"The current conversion rate from INR to USD is: {itur}")

sps['Salary USD'] = (sps['Salary'].astype(int) * itur).astype(int)
print(sps[['Salary', 'Salary USD']].head())

# Objective 8: Calculate the average `Salary USD` for the `Python` Job Role.
pjr = sps[sps['Job Roles'] == 'Python']
avup = pjr['Salary USD'].mean()
print(f"The average Salary USD for the Python Job Role is: {avup}")

# Objective 9: Identify the `Company Name` with the highest average `Salary USD` across all `Job Titles`.
avg_sal = sps.groupby('Company Name')['Salary USD'].mean()
hasc = avg_sal.idxmax()
print(f"The Company with the highest average Salary USD is: {hasc}")

# Objective 10: Visualize the relationship between the average `Salary USD` and the average `Rating` for each `Company Name`.
average_salaries = sps.groupby('Company Name')['Salary USD'].mean()
average_ratings = sps.groupby('Company Name')['Rating'].mean()

plot_sps = pd.DataFrame({
    'Company Name': average_salaries.index,
    'Average Salary USD': average_salaries.values,
    'Average Rating': average_ratings.values
})

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Average Salary USD', y='Average Rating', s=50, alpha=0.8, data=plot_sps)
plt.title('Relationship between Average Salary and Rating for each Company')
plt.xlabel('Average Salary (USD)')
plt.ylabel('Average Rating')
plt.show()

# Final Considerations
print("FINAL CONSIDERATIONS: 'Thapar University' stands out with an exceptionally high average salary of 1,078,110 USD but a relatively low rating of 3.6.")
print("This creates a sharp contrast with the second company, 'FFF Enterprises', which has a salary of 117,394 USD and a rating of 4.2. From the second company onwards, the salary drops are relatively linear.")
