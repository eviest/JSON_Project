import json

in_file = open('US_fires_9_1.json', 'r')


# do I need this?
out_file = open('readable_US_fires_9_1.json', 'w') 

fire_data = json.load(in_file)            

json.dump(fire_data, out_file, indent=4)

list_of_fires = fire_data['features'] 

print(type(list_of_fires))

print(len(list_of_fires))

