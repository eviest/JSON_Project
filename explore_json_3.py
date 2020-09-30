import json                 # creating more hover text

in_file = open('eq_data_30_day_m1.json', 'r')

out_file = open('readable_eq_data.json', 'w') 

eq_data = json.load(in_file)            #eq_data is a format python can use

json.dump(eq_data, out_file, indent=4)

list_of_eqs = eq_data['features']           # we gave the key 'features' and it will return the value

print(type(list_of_eqs))                    # we figured out it's a list

# how many earthquakes do we have? every obj in list is an earthquake
print(len(list_of_eqs))

# create 3 lists
mags,lons,lats, hover_texts = [],[],[],[]

# iterate through list_of_eqs
for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    title = eq['properties']['title']
    # brightness can be found like how these values were found
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# print statement I made to figure out how to iterate above
# print(list_of_eqs[0]['properties']['mag'])

print("Mags")
print(mags[:10])            # print first 10 in list -- if you give the upper end, it will start at 0
print("Lons")
print(lons[:10])
print("Lats")
print(lats[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# lon and lat are arguments that Scattergeo needs to plot something
#data = [Scattergeo(lon=lons, lat=lats)]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size':[5*mag for mag in mags],                        # list comprehension -- easy way to create a list
        'color':mags,                                          # the output is a list as well -- it's a for loop in the list
        'colorscale':'Viridis',                                # for each mag in mags, multiply mag*5 -- it produces a list of answers
        'reversescale':True,                                   # flip the set colors
        'colorbar':{'title':'Magnitude'}
    }
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout':my_layout}

# we're using offline bc we don't have a server running
offline.plot(fig, filename='global_earthquakes.html')