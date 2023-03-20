import googlemaps
import pprint

gmaps = googlemaps.Client(key='AIzaSyD9HmY5GR0zaOef0TBODBGIwjUNlmqC9HI')
place_id = gmaps.find_place(input='sezamkowa 14, olmonty',
                            input_type="textquery")['candidates'][0]['place_id']

address_components = gmaps.place(place_id)['result']['address_components']
"""
pprint.pprint(address_components)


[
 {'long_name': '7', 'short_name': '7', 'types': ['street_number']},
 {'long_name': 'Harcerska', 'short_name': 'Harcerska', 'types': ['route']},
 {'long_name': 'Kawaleryjskie',
  'short_name': 'Kawaleryjskie',
  'types': ['sublocality_level_1', 'sublocality', 'political']},
 {'long_name': 'Białystok',
  'short_name': 'B-stok',
  'types': ['locality', 'political']},
 {'long_name': 'Białystok',
  'short_name': 'Białystok',
  'types': ['administrative_area_level_2', 'political']},
 {'long_name': 'Podlaskie',
  'short_name': 'Podlaskie',
  'types': ['administrative_area_level_1', 'political']},
 {'long_name': 'Poland', 'short_name': 'PL', 'types': ['country', 'political']},
 {'long_name': '15-345', 'short_name': '15-345', 'types': ['postal_code']}
]
"""

#(lenght,(i, long name))

maxLen = (0, (0, ''))

for dictionary in address_components:
    types = dictionary['types'][0]
    name = dictionary['long_name']
    lenght = len(name)

    if lenght > maxLen[0]:
        maxLen = (lenght, (name, types))
        
print(maxLen[1])


