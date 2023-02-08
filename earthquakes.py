'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude,
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''

import json
eqfile = open('eq_data.json', 'r')
earthquakes_dict = json.load(eqfile)
# print(type(earthquakes_dict))
# returns <class 'dict'>

# 1) Number of earthquakes
eqnum = earthquakes_dict['metadata']['count']
features_length = (len(earthquakes_dict['features']))
print(f"The number of earthquakes in the data set is {eqnum}")
# eqnum and features_length give same number of earthquakes
print('\n')
# 2) New dictionary
eq_dict = {}
earthquakes = earthquakes_dict['features']
# print(type(earthquakes))
# class dict
counter = 1
for quake in earthquakes:
    if quake['properties']['mag'] > 6:
        quake_dict = {}
        quake_dict['location'] = quake['properties']['place']
        quake_dict['magnitude'] = quake['properties']['mag']
        quake_dict['coordinates'] = quake['geometry']['coordinates']
        eq_dict[f"earthquake {counter}"] = quake_dict
        counter += 1
print(eq_dict)
print('\n')


# 3)
for quake in eq_dict:
    print(f"Location: {eq_dict[quake]['location']}")
    print(f"Magnitude: {eq_dict[quake]['magnitude']}")
    print(f"Longitude: {eq_dict[quake]['coordinates'][0]}")
    print(f"Latitude: {eq_dict[quake]['coordinates'][1]}")
    print()
