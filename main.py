'''Use Google Maps GeoCoding API to get a place's 
    latitude and longitude as well as formatted address.
    With both latitude and longitude, we can put a marker on the
    map  for that address'''
import urllib.parse, urllib.request
import json

# retrieve the api key from a secret file
with open('google_map.txt', 'r')  as file:
    key = file.read().split()[2].strip()

def get_lat_lng(address):

    # get base_url from google map api doc
    base_url = f'https://maps.googleapis.com/maps/api/geocode/json?'
    # use urllib library for converting dic into query string
    query_url = urllib.parse.urlencode({'address': address, 'key': key})
    url = base_url + query_url

    # send request to the url and get response
    with urllib.request.urlopen(url) as response:
        # read response (HTTPResponse) into bytes, then string, then dict (json)        
        data = json.loads(response.read().decode())
        # in case address provided is not real
        if data['status'] != 'OK' or 'status' not in data:
            data = None

    # To read the json file
    # print(json.dumps(data, indent=4))

    # To check the request status
    # print(data['status'])

    # to get lat and lng
    if data != None:
        location= data['results'][0]['geometry']['location']
        lat = location['lat']
        lng = location['lng']
        formatted_address = data['results'][0]['formatted_address']
        return lat, lng, formatted_address
    else:
        print('try again')
        return 

print(get_lat_lng("sumiao juancheng"))