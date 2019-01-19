import requests, urllib

API_KEY = "AIzaSyA004RB-WTpFX21l593l7dF9G6A7nh3a_8"
URL = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Seattle&destinations=San+Francisco&key=" + API_KEY

def get_distance(origin, dest):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?' # add a ? behind the API url
    dic = {}
    dic['origins'] = origin
    dic['destinations'] = dest
    key = API_KEY
    url += urllib.parse.urlencode(dic) #use urllib.parse.urlencode to pass in the required parameters
    data = requests.get(url).json()  # use requests library to get data and load the JSON into a Python usable format
    distance = data['rows'][0]['elements'][0]['distance']['value']
    return distance

def get_distance_coord(origin_lat, origin_long, dest_lat, dest_long):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'  # add a ? behind the API url
    dic = {}
    dic['origins'] = str(origin_lat) + "," + str(origin_long)
    dic['destinations'] = str(dest_lat) + "," + str(dest_long)
    key = API_KEY
    url += urllib.parse.urlencode(dic)  # use urllib.parse.urlencode to pass in the required parameters
    data = requests.get(url).json()  # use requests library to get data and load the JSON into a Python usable format
    distance = data['rows'][0]['elements'][0]['distance']['value']
    return distance

def to_coord(place):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    url += urllib.parse.urlencode({'key' : API_KEY, 'address' : place})
    data = requests.get(url).json()
    print(data)
    coords = data['results'][0]['geometry']['location']
    coords = (coords['lat'], coords['lng'])
    return coords

#print(to_coord("1600 Amphitheatre Parkway, Mountain View, CA"))