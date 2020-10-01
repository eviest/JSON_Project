import json

in_file = open('US_fires_9_14.json', 'r')

out_file = open('readable_US_fires_9_14.json', 'w') 

fire_data = json.load(in_file)            

json.dump(fire_data, out_file, indent=4)

list_of_fires = fire_data

brights,lons,lats= [],[],[]

# iterate through list_of_fires
for fire in list_of_fires:
    bright = fire['brightness']
    lon = fire['longitude']
    lat = fire['latitude']
    
    if bright > 450:
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size':[bright/30 for bright in brights],                        
        'color':brights,                                          
        'colorscale':'Viridis',                                
        'reversescale':True,                                  
        'colorbar':{'title':'Magnitude'}
    }
}]

my_layout = Layout(title='US Fires 9/14/2020 through 9/20/2020')

fig = {'data': data, 'layout':my_layout}

offline.plot(fig, filename='us_fires.html')
