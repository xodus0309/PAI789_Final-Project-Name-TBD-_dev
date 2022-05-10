# Initial setting.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('co-est2021-alldata.csv', dtype={'STATE': str, 'COUNTY': str})
df['STATE'] = df['STATE'].str.rjust(2, '0')
df['COUNTY'] = df['COUNTY'].str.rjust(3, '0')
df['geoid'] = df['STATE'] + df['COUNTY']
df['name'] = df['CTYNAME'] + ', ' + df['STNAME']
df['pop'] = df['POPESTIMATE2021']
df = df[['geoid', 'name', 'pop']]
df1 = df.set_index('name')
df1.to_csv('total pop.csv')
print(df1)

df2 = pd.read_csv('LND01.csv', dtype={'STCOU': str})
df2['STCOU'] = df2['STCOU'].str.rjust(5, '0')
df2['geoid'] = df2['STCOU']
df2['area'] = df2['LND010190F'] + df2['LND010190D'] + \
    df2['LND010190N1'] + df2['LND010190N2']
df2 = df2[['Areaname', 'geoid', 'area']]
df2 = df2.set_index('Areaname')
df2.to_csv('land area.csv')
print(df2)

df3 = df.set_index('geoid').join(df2.set_index('geoid'))
df3['density'] = df3['pop'] / df3['area']
df3 = df3.sort_values(by=['density'], ascending=False)
df3.to_csv('density.csv')
df3 = df3.head(9)
df3 = df3.set_index('name')
print(df3)

fig1, ax1 = plt.subplots(dpi=300)
bars = ['density']
df3[bars].plot.bar(ax=ax1)
fig1.suptitle('Top 9 Counties in Population Density')
ax1.set_xlabel('County')
ax1.set_ylabel('Density')
fig1.tight_layout()
fig1.savefig('Pop Density.png')
