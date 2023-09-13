#import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import dataset
df = pd.read_csv('Ichiro.csv')

#exploring data
df.shape

df.info()

df.isna().sum()

df.columns

df.head()

df.describe()

def exploratory_visuals(df, column_names):
  for col in column_names:
    if pd.api.types.is_numeric_dtype(df[col]):
      plt.hist(df[col])
      plt.title(f'Histogram of {col}')
      plt.xlabel(col)
      plt.ylabel('Count')
      plt.show()
    else:
      df[col].value_counts().plot(kind = 'bar')
      plt.title(f'Bar chart of {col}')
      plt.xlabel(col)
      plt.ylabel('Count')
      plt.show()

plt.style.use('seaborn-v0_8')

exploratory_visuals(df,df.columns)

#Cleaning and preprocessing
#there are 3 rows for 2012. Keep the row with the total and remove the other two

delete_rows = [12, 13]
df = df.drop(delete_rows, axis = 0)

df.at[11, 'Tm'] = 'SEA_NYY'

df[['Year', 'Tm']]

#Analysis and visualizations

#Which 5 years were Ichiros most productive offensive years?
#Top 5 years with highest batting average

top_ba = df.groupby(['Year', 'BA']).size().reset_index()
top_ba = df.sort_values(by = 'BA', ascending = False).head(5)

top5_ba =top_ba[['Year', 'BA']]

print(top5_ba)

mariners_colors = ['#0C2C56','#005C5C']

#create barplot
plt.figure(figsize=(12, 6))

sns.barplot(x ='Year', y ='BA', data = top5_ba, palette = mariners_colors)
plt.xlabel('Year')
plt.ylabel('Batting Average (BA)')
plt.title('Top 5 Years with Highest Batting Averages')

# Display the plot
plt.show()

#Top 5 years with highest OPS+
#OPS + is the on base percenage + the slugging percentage adjusted for the ballparks

top_ops_plus = df.groupby(['Year', 'OPS+']).size().reset_index()
top_ops_plus = df.sort_values(by = 'OPS+', ascending = False).head(5)

top5_ops_plus = top_ops_plus[['Year', 'OPS+']]

print(top5_ops_plus)

colors = ['#002878','#FFCC00']

#create barplot
plt.figure(figsize=(12, 6))

sns.barplot(x ='Year', y ='OPS+', data = top5_ops_plus, palette = colors)
plt.xlabel('Year')
plt.ylabel('On-base Plus Slugging + (OPS+)')
plt.title('Top 5 Years with Highest OPS+')

# Display the plot
plt.show()

#Top 5 years with most runs batted in (RBI)

top_rbi = df.groupby(['Year', 'RBI']).size().reset_index()
top_rbi = df.sort_values(by = 'RBI', ascending = False).head(5)

top5_rbi = top_rbi[['Year', 'RBI']]

print(top5_rbi)

#create barplot

plt.figure(figsize=(12, 6))
sns.barplot(x ='Year', y ='RBI', data = top5_rbi, palette = mariners_colors)
plt.xlabel('Year')
plt.ylabel('Runs batted in (RBI)')
plt.title('Top 5 Years with most RBI')

# Display the plot
plt.show()

#top 5 years with most runs scored

top_run = df.groupby(['Year', 'R']).size().reset_index()
top_runs = df.sort_values(by = 'R', ascending = False).head(5)

top5_runs = top_runs[['Year', 'R']]

print(top5_runs)

#create barplot
plt.figure(figsize=(12, 6))

sns.barplot(x ='Year', y ='R', data = top5_runs, palette = colors)
plt.xlabel('Year')
plt.ylabel('Runs scored')
plt.title('Top 5 Years with most runs scored')

#display plot
plt.show()

#Graph the most productive years

#concat dataframe
top5_years = pd.concat([top5_ba, top5_ops_plus, top5_rbi, top5_runs])

# Melt the dataframe
top_years = pd.melt(top5_years, id_vars='Year', var_name='Offense')
top_years = top_years.dropna()

#create barplot
plt.figure(figsize=(12, 6))
sns.barplot(data=top_years, x='Year', y='value', hue='Offense', palette='viridis')

plt.title("Most Productive Years")
plt.xlabel('Year')
plt.ylabel('Total Value')
plt.legend(title="Offense", loc='upper left', bbox_to_anchor=(1, 1))

#display plot
plt.show()
