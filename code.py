# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(path)
data.rename(columns = {'Total': 'Total_Medals'}, inplace=True)

# Summer or Winter
data['Better_Event'] = np.where(
    data['Total_Summer'] > data['Total_Winter'], 'Summer',
    np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', 'Winter'))

better_event = data['Better_Event'].value_counts().index[0]

# Top 10
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

""" top_countries = top_countries.drop(['Total_Medals'], axis=1) """

def top_ten(df, col):
    country_list = list(df.nlargest(11, col)['Country_Name'])[1:]
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

common = []

for i in range(10):
    if top_10[i] in top_10_summer and top_10[i] in top_10_winter:
        common.append(top_10[i])

# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

fig, axs = plt.subplots(nrows=3, figsize=(10, 10))
fig.subplots_adjust(hspace=.5)
                                          
axs[0].bar(summer_df['Country_Name'], summer_df['Total_Summer'])
axs[1].bar(winter_df['Country_Name'], winter_df['Total_Winter'])
axs[2].bar(top_df['Country_Name'], top_df['Total_Medals'])

plt.sca(axs[0])
plt.xticks(rotation=30)
plt.sca(axs[1])
plt.xticks(rotation=30)
plt.sca(axs[2])
plt.xticks(rotation=30)

plt.show()

# Top Performing Countries
summer_df['Golden_Ratio'] = (summer_df['Gold_Summer'] /
                             summer_df['Total_Summer'])

summer_max = summer_df[summer_df['Golden_Ratio'] ==
                       summer_df['Golden_Ratio'].max()]
summer_max_ratio = summer_max['Golden_Ratio']
summer_country_gold = summer_max['Country_Name']


winter_df['Golden_Ratio'] = (winter_df['Gold_Winter'] /
                             winter_df['Total_Winter'])

winter_max = winter_df[winter_df['Golden_Ratio'] ==
                       winter_df['Golden_Ratio'].max()]
winter_max_ratio = winter_max['Golden_Ratio']
winter_country_gold = winter_max['Country_Name']


top_df['Golden_Ratio'] = (top_df['Gold_Total'] /
                             top_df['Total_Medals'])

top_max = top_df[top_df['Golden_Ratio'] ==
                       top_df['Golden_Ratio'].max()]

top_max_ratio = round(top_max['Golden_Ratio'], 2)
top_country_gold = str(top_max['Country_Name'])


# Best in the world 
data1 = data.drop(columns=['Total_Medals'])
data1['Total_Points'] = (data1['Gold_Total'] * 3 + data1['Silver_Total'] * 2 +
                         data1['Bronze_Total'])

max_points = data1['Total_Points'][:-1].idxmax()
most_points = data1.iloc[max_points]['Total_Points']
best_country = data1.iloc[max_points]['Country_Name']

# Plotting the best
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(xticks=[],stacked=True, figsize=(10,10))
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


