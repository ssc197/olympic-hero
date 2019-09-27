# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data = data.rename(columns = {'Total':'Total_Medals'})

print (data.head(10))


# --------------
#Code starts here
data['Better_Event']  = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', (np.where(data['Total_Summer'] < data['Total_Winter'], 'Winter', 'Summer')))

better_event = data['Better_Event'].value_counts().idxmax()

print (better_event)


# --------------
#Code starts here
top_countries =  data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]


top_countries.drop(top_countries.tail(1).index,inplace=True) # drop last n rows

def top_ten(top_countries,colname):
    country_list=[]
    _topten = top_countries.nlargest(10,colname)
    country_list = _topten['Country_Name']
    return country_list

top_10_summer = list(top_ten(top_countries,'Total_Summer'))
top_10_winter = list(top_ten(top_countries,'Total_Winter'))
top_10 = list(top_ten(top_countries,'Total_Medals'))

my_list = [top_10_summer,top_10_winter,top_10]

common = list(set.intersection(*map(set, my_list)))
print (common)


# --------------
#Code starts here
fig, (ax_1,ax_2, ax_3) = plt.subplots(nrows = 3, ncols = 1)


summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]


summer_df = summer_df[['Country_Name','Total_Summer']]

#summer_df.set_index(['Country_Name'], inplace = True)

winter_df = winter_df[['Country_Name','Total_Winter']]
#winter_df.set_index(['Country_Name'], inplace = True)

top_df = top_df[['Country_Name','Total_Medals']]
#top_df.set_index(['Country_Name'], inplace = True)


summer_df.plot(kind='bar', ax=ax_1)
ax_1.set_title('Summer Medals')

winter_df.plot(kind='bar', ax=ax_2)
ax_2.set_title('Winter Medals')

top_df.plot(kind='bar', ax=ax_3)
ax_3.set_title('Top Medals')




# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']  / summer_df['Total_Summer']

summer_df.set_index('Country_Name', inplace=True)

summer_max_ratio =summer_df['Golden_Ratio'].max()
print ('Summer Max Gold:',summer_max_ratio)
summer_country_gold  = summer_df['Golden_Ratio'].idxmax()
print ('Summer Country Gold:',summer_country_gold)

#For Winter------------------------------------------ 

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']  / winter_df['Total_Winter']

winter_df.set_index('Country_Name', inplace=True)

winter_max_ratio =winter_df['Golden_Ratio'].max()
print ('Winter Max Gold:',winter_max_ratio)
winter_country_gold  = winter_df['Golden_Ratio'].idxmax()
print ('Winter Country Gold:',winter_country_gold)

#For Top medals-------------------------------------

top_df['Golden_Ratio'] = top_df['Gold_Total']  / top_df['Total_Medals']

top_df.set_index('Country_Name', inplace=True)

top_max_ratio =top_df['Golden_Ratio'].max()
print ('Top Max Ratio:',top_max_ratio)
top_country_gold  = top_df['Golden_Ratio'].idxmax()
print ('Top Gold Country:',top_country_gold)



# --------------
#Code starts here
data_1 = data[:-1]
#data_1.set_index('Country_Name', inplace=True)
data_1['Total_Points'] = (data_1['Gold_Total']*3)+ (data_1['Silver_Total']*2)+ data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points'].idxmax(), 'Country_Name']
print ('Most points:',most_points)
print ('Best Country:',best_country)


# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot(kind='bar', stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)



