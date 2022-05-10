# Initial setting.

import pandas as pd
import matplotlib.pyplot as plt

# Import average number of cases of recent 7 days.

df = pd.read_csv('us-counties-recent.csv')
df = df.query("date == '2022-05-08'")
df = df.drop(columns=['date'])
df = df.rename(columns={'cases_avg': 'c_avg', 'cases_avg_per_100k': 'c_avg_100',
                        'deaths_avg': 'd_avg', 'deaths_avg_per_100k': 'd_avg_100'})

# Derive top 10 counties.

df1 = df.sort_values(by=['c_avg_100'], ascending=False)
df1 = df1.drop(columns=['deaths', 'd_avg', 'd_avg_100'])
df1['geoid'] = df1['geoid'].str.replace('USA-', '')
df1['name'] = df1['county'] + ', ' + df1['state']
df1 = df1.set_index('name')
df1.to_csv('covid cases per capita.csv')
df1 = df1.head(10)
print(df1)
df2 = df.sort_values(by=['d_avg_100'], ascending=False)
df2 = df2.drop(columns=['cases', 'c_avg', 'c_avg_100'])
df2['geoid'] = df2['geoid'].str.replace('USA-', '')
df2['name'] = df2['county'] + ', ' + df2['state']
df2 = df2.set_index('name')
df2.to_csv('death cases per capita.csv')
df2 = df2.head(10)
print(df2)

# Create figures.

fig1, ax1 = plt.subplots(dpi=300)
bars = ['c_avg_100']
df1[bars].plot.bar(ax=ax1)
fig1.suptitle('Top 10 Counties of Covid Cases')
ax1.set_xlabel('County')
ax1.set_ylabel('Number of Cases')
fig1.tight_layout()
fig1.savefig('Covid Cases.png')
fig2, ax2 = plt.subplots(dpi=300)
bars = ['d_avg_100']
df2[bars].plot.bar(ax=ax2)
fig2.suptitle('Top 10 Counties of Covid Deaths')
ax2.set_xlabel('County')
ax2.set_ylabel('Number of Deaths')
fig2.tight_layout()
fig2.savefig('Covid Deaths.png')
