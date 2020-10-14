import pandas as pd
import numpy as np

# Importing both parts, concat them and remove duplicates
df1 = pd.read_csv('glassdoor_data_pt1.csv')
df2 = pd.read_csv('glassdoor_data_pt2.csv')
df = pd.concat([df1, df2], ignore_index=True)
df = df.drop_duplicates(ignore_index=True)

# Dropping Columns with no data
df.isnull().sum()
df.drop(['Headquarters', 'Competitors'], axis=1, inplace=True)

# Removing Rows With no Salary Estimative
df = df[~df['Salary Estimate'].isnull()]

# Salary
## Flag Hourly
df['hourly_salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
## Removing unnecessary words
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.replace('$', '').replace('K', '').replace('\r', '').replace('\n', ''))
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.lower().replace('employer provided salary:', ''))
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.lower().replace('per hour', ''))
## Break min/max and calculate avg salary
df['min_salary'] = pd.to_numeric(df['Salary Estimate'].apply(lambda x: x.split('-')[0]))
df['min_salary'] = df.apply(lambda x: x['min_salary'] if x['hourly_salary'] != 1 else x['min_salary']*2, axis=1) #Convert to yearly salary
df['max_salary'] = pd.to_numeric(df['Salary Estimate'].apply(lambda x: x.split('-')[1]))
df['max_salary'] = df.apply(lambda x: x['max_salary'] if x['hourly_salary'] != 1 else x['max_salary']*2, axis=1) #Convert to yearly salary
df['avg_salary'] = ( df['min_salary'] + df['max_salary'] ) / 2

# Company Name
df['Company Name'] = df.apply(lambda x: x['Company Name'].replace(str(x['Rating']), '').replace('\n', '').replace('\r', ''), axis=1)

# Export Cleaned Data
df.to_csv('glassdoor_data_cleaned.csv', index=False)