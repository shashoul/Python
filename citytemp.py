"""
 Following program get as input 
 city name and print the temperature 
 and humidity of that city.
"""

import requests

def get_request_jason(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        # This means something went wrong.
        raise requests.RequestException('GET ERROR {}'.format(resp.status_code))
    j_resp = resp.json()
    return j_resp


#city = input("Please Enter you city:")
city="haifa"

#resp_map = get_request_jason('http://maps.googleapis.com/maps/api/geocode/json?address='
#+ city)
resp_map = get_request_jason('http://maps.googleapis.com/maps/api/geocode/json?address="haifa"')


dic1 = (resp_map['results'])[0]
cor1 = str(dic1['geometry']['location']['lat'])
cor2 = str(dic1['geometry']['location']['lng'])
print("Your City: " + city )
print("City cordinators: " + cor1 + ' ' + cor2)
print("============================================")

j_whether = get_request_jason('https://api.darksky.net/forecast/0d584daf877a4ff2998afe4329840ef9/'+
cor1 +',' + cor2)

print("Your City temperature: " , j_whether['currently']['temperature'])
print("Your City humidity: " , j_whether['currently']['humidity'])


