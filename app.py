# Day 80 - Dr. Semmelweis: Vienna Childbirth Analysis (Complete Project)

# Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import matplotlib.dates as mdates
import plotly.express as px

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (14,6)

# Step 2: Load CSV files
df_monthly = pd.read_csv('monthly_deaths.csv')
df_yearly = pd.read_csv('annual_deaths_by_clinic.csv')

# Convert 'date' column in monthly data to datetime
df_monthly['date'] = pd.to_datetime(df_monthly['date'])

# ------------------------------
# Challenge 1: Preliminary Exploration
# ------------------------------
print("Monthly data shape:", df_monthly.shape)
print("Yearly data shape:", df_yearly.shape)
print("\nMonthly columns:", df_monthly.columns.tolist())
print("Yearly columns:", df_yearly.columns.tolist())
print("\nYears in yearly dataset:", df_yearly['year'].unique())
print("\nMonthly NaNs:", df_monthly.isna().values.any())
print("Yearly NaNs:", df_yearly.isna().values.any())
print("Monthly duplicates:", df_monthly.duplicated().values.any())
print("Yearly duplicates:", df_yearly.duplicated().values.any())
print("\nAverage births per month:", df_monthly['births'].mean())
print("Average deaths per month:", df_monthly['deaths'].mean())

# ------------------------------
# Challenge 2: Percentage of Women Dying in Childbirth (1840s Vienna)
# ------------------------------
mortality_percent = df_yearly['deaths'].sum() / df_yearly['births'].sum() * 100
print(f"\nPercentage of women dying in childbirth (1840s Vienna): {mortality_percent:.3f}%")
print("Compare to US 2013: 0.018%")

# ------------------------------
# Challenge 3: Monthly Births and Deaths Twin-axis Plot
# ------------------------------
plt.figure(figsize=(14,8), dpi=200)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.grid(color='grey', linestyle='--')

# Plot births
ax1.plot(df_monthly['date'], df_monthly['births'], color='skyblue', linewidth=3, label='Births')
# Plot deaths
ax2.plot(df_monthly['date'], df_monthly['deaths'], color='crimson', linewidth=2, linestyle='--', label='Deaths')

# Configure x-axis with locators
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

ax1.set_xlim([df_monthly['date'].min(), df_monthly['date'].max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.set_ylabel('Births', color='skyblue', fontsize=16)
ax2.set_ylabel('Deaths', color='crimson', fontsize=16)
ax1.tick_params(axis='y', labelcolor='skyblue')
ax2.tick_params(axis='y', labelcolor='crimson')
ax1.tick_params(axis='x', rotation=45)

plt.show()
print("\nObservation: Mortality sharply decreased after 1847, while births continued increasing.")

# ------------------------------
# Challenge 4: Yearly Data Split by Clinic (Plotly)
# ------------------------------
# Total yearly births by clinic
fig_births = px.line(df_yearly,
                     x='year',
                     y='births',
                     color='clinic',
                     title='Total Yearly Births by Clinic',
                     markers=True)
fig_births.show()

# Total yearly deaths by clinic
fig_deaths = px.line(df_yearly,
                     x='year',
                     y='deaths',
                     color='clinic',
                     title='Total Yearly Deaths by Clinic',
                     markers=True)
fig_deaths.show()

# Summary stats
clinic1_births_total = df_yearly[df_yearly['clinic']=='clinic 1']['births'].sum()
clinic2_births_total = df_yearly[df_yearly['clinic']=='clinic 2']['births'].sum()
print(f"Total births clinic 1: {clinic1_births_total}")
print(f"Total births clinic 2: {clinic2_births_total}")
max_deaths_c1 = df_yearly[df_yearly['clinic']=='clinic 1']['deaths'].max()
max_deaths_c2 = df_yearly[df_yearly['clinic']=='clinic 2']['deaths'].max()
print(f"Highest deaths clinic 1: {max_deaths_c1}")
print(f"Highest deaths clinic 2: {max_deaths_c2}")

# ------------------------------
# Challenge 5: Proportion of Deaths per Clinic
# ------------------------------
df_yearly['pct_deaths'] = df_yearly['deaths'] / df_yearly['births'] * 100

clinic1 = df_yearly[df_yearly['clinic']=='clinic 1']
clinic2 = df_yearly[df_yearly['clinic']=='clinic 2']

avg_c1 = clinic1['deaths'].sum() / clinic1['births'].sum() * 100
avg_c2 = clinic2['deaths'].sum() / clinic2['births'].sum() * 100
print(f"Average death rate in clinic 1: {avg_c1:.2f}%")
print(f"Average death rate in clinic 2: {avg_c2:.2f}%")

# Plot yearly percentage deaths
fig_pct = px.line(df_yearly,
                  x='year',
                  y='pct_deaths',
                  color='clinic',
                  title='Proportion of Yearly Deaths by Clinic',
                  markers=True)
fig_pct.show()

# Highest yearly death rates
max_pct_c1 = clinic1['pct_deaths'].max() * 100
max_pct_c2 = clinic2['pct_deaths'].max() * 100
print(f"Highest yearly death rate clinic 1: {max_pct_c1:.2f}%")
print(f"Highest yearly death rate clinic 2: {max_pct_c2:.2f}%")

# ------------------------------
# Step 6: Reflection / Story Context
# ------------------------------
print("""
Observations:
- Clinic 1 (male doctors) had more births and deaths than Clinic 2 (midwives).
- Average death rate clinic 1: {:.2f}%, clinic 2: {:.2f}%.
- Highest mortality year in clinic 1: {:.2f}%, clinic 2: {:.2f}%.
- Clinic 2 consistently had lower death rates.

Story Context:
- Dr. Semmelweis initially tested birth position and priestly bell ringing as causes.
- After a colleague's death, he realized cadaver particles caused childbed fever.
- This led to handwashing with chlorinated solutions, drastically reducing mortality.
""".format(avg_c1, avg_c2, max_pct_c1, max_pct_c2))
