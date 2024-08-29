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

# Question 1: What is the shape (rows, cols) of the `sps` DataFrame?
print(sps.shape)

# Question 2: How many unique `Job Roles` are there in the dataset?
print(sps['Job Roles'].nunique())
print(sps['Job Roles'].unique())

# Question 3: How many unique `Job Title` are there for the "Python" `Job Role`?
python_role = sps[sps['Job Roles'] == 'Python']
upjt = python_role['Job Title'].nunique()
print("Numero di ruoli Python in Job Titles:", upjt)

# Question 4: Of the `Company Name`s that are listed in the DataFrame, how many have a "Python" `Job Role` with a `Job Title` containing the substring "Analyst"?
par = sps[(sps['Job Roles'] == 'Python') & sps['Job Title'].str.contains('Analyst', case=False)]
ucpa = par['Company Name'].nunique()
print('Le aziende che hanno Python come Job Role con un Job Title contenente la parola "Analyst" sono:', ucpa)

# Question 5: Which `Company Name` has the highest number of `Salaries Reported` (across all `Job Title`s)?
ssc = sps.groupby('Company Name')['Salaries Reported'].sum()
cms = ssc.idxmax()
ms = ssc.max()
print(f"La Company Name con il numero più alto di Salaries Reported è '{cms}' con un totale di {ms} di reports.")

# Question 6: Given the `Company Name` you found at the previous question, how many `Location`s is this company present in?
csl = sps[sps['Company Name'] == 'Amazon']
ulc = csl['Location'].nunique()
print(f"L'azienda Amazon è presente in {ulc} città")

# Question 7: Create a new column named `Salary USD` containing the salary-equivalent in USD
def get_inr_to_usd_rate():
    url = "https://open.er-api.com/v6/latest/INR"
    r = requests.get(url)
    data = r.json()
    if r.status_code == 200:
        return data['rates']['USD']
    else:
        return "Tasso di conversione assente!"

itur = get_inr_to_usd_rate()
print(f"l'attuale conversione di Rupie(INR) in Dollari(USD) è: {itur}")

sps['Salary USD'] = (sps['Salary'].astype(int) * itur).astype(int)
print(sps[['Salary', 'Salary USD']].head())

# Question 8: What is the average `Salary USD` for the "Python" `Job Role`?
pjr = sps[sps['Job Roles'] == 'Python']
avup = pjr['Salary USD'].mean()
print(f"The average Salary USD for the Python Job Role is: {avup}")

# Question 9: Which `Company Name` has the highest average `Salary USD` across all `Job Title`s?
avg_sal = sps.groupby('Company Name')['Salary USD'].mean()
hasc = avg_sal.idxmax()
print(f"L'Azienda con il salario medio più alto è: {hasc}")

# Question 10: Create a Plot that shows the relationship between the average `Salary USD` and the average `Rating` for each `Company Name`
average_salaries = sps.groupby('Company Name')['Salary USD'].mean()
average_ratings = sps.groupby('Company Name')['Rating'].mean()

plot_sps = pd.DataFrame({
    'Company Name': average_salaries.index,
    'Average Salary USD': average_salaries.values,
    'Average Rating': average_ratings.values
})

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Average Salary USD', y='Average Rating', s=50, alpha=0.8, data=plot_sps)
plt.title('Relazione tra la media del Salario ed il Rating per ogni Azienda')
plt.xlabel('Salario Medio (USD)')
plt.ylabel('Rating Medio')
plt.show()

# Considerazioni finali
print("CONSIDERAZIONI: La 'Thapar University' spicca fuori dagli schemi per salario medio con valori di 1.078.110 ma con rating 3.6")
print("che da uno stacco di rapporto 1:10 dal secondo 'FFF Enterprises' con 117.394 rating 4.2. Dal secondo in poi le discese sono abbastanza lineari.")
