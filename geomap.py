# !pip install descartes
import pandas as pd
import geopandas as gpd
import matplotlib as mpl
# mpl.use('Agg')
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import style
print(gpd.datasets.available)
pd.set_option('display.max_columns',None)


import pycountry

convert = {}
for country in pycountry.countries:
    convert[country.alpha_3] = country.alpha_2
    
country=pd.read_csv('country.csv')

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
world["area"] = world.area
world['centroid'] = world.centroid
# print(world)
print(len(convert))
# world.plot(figsize=(20,20))
# plt.show()

world['iso_a2'] = world['iso_a3'].apply(lambda x:convert.get(x,'ZZ'))

# print(world)

co2=country[['country','count']]
#print(co2)
world=world.merge(co2,left_on='iso_a2',right_on='country',how='outer')

# world.plot(column='CO2 emission estimates (million tons/tons per capita)', figsize=(20,20))

# world.plot(column='CO2 emission estimates (million tons/tons per capita)',figsize=(20,10),legend=True,legend_kwds={'label': "CO2 Emission Per Capita",'orientation': "horizontal"})

# world.plot(column='CO2 emission estimates (million tons/tons per capita)',figsize=(20,10),legend=True,legend_kwds={'label': "CO2 Emission Per Capita",'orientation':"horizontal"},missing_kwds={'color': 'lightgrey'})

base=world.boundary.plot(figsize=(20,10),edgecolor='black')
world.plot(ax=base,column='count',figsize=(20,10),legend=True,legend_kwds={'label': "Victim",'orientation':"vertical"},missing_kwds={'color': 'lightgrey'},cmap='RdYlGn_r')
plt.show()
plt.savefig('hijacker_country.png')