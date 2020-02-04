#! /usr/bin/env python3
# coding: UTF-8

from requests import get
from config import API_KEY

class GmapsRequest:

    def __init__(self, user_request):

        self.gkey = API_KEY
        self.user_request = user_request
        self.data = {}

        self.request_api()

    def request_api(self):

        url = "https://maps.googleapis.com/maps/api/geocode/json"
        
        params = {
            'address': self.user_request,
            'key': self.gkey,
            'region':'fr'
        }

        request = get(url=url, params=params)
        result = request.json()
        
        if result['status'] == "OK":
            self.data = {
                "status": result['status'],
                "lat": result['results'][0]['geometry']['location']['lat'],
                "lng": result['results'][0]['geometry']['location']['lng'],
                "address": result['results'][0]['formatted_address']
            }
        else:
            self.data = {
                "status": result['status']
            }

        return self.data
        
class MediawikiRequest:
   
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.story = ""
        self.request_api()

    def request_api(self):

        url = "https://fr.wikipedia.org/w/api.php"

        params = {
            'action':"query",
            'list':"geosearch",
            'gscoord': str(self.latitude) + "|" + str(self.longitude),
            'gsradius':500,
            'gslimit':1,
            'format':"json"
        }
        request = get(url=url, params=params)
        result = request.json()

        places = result['query']['geosearch']
        title = places[0]['title']
        
        params = {
            'action':"query",
            'exsentences':2,
            'exlimit':2,
            'explaintext':True,
            'exsectionformat':'plain',
            'titles': title,
            'format':"json",
            'prop':"extracts|info",
            'inprop': 'url'
        }
        request = get(url=url, params=params)
        result = request.json()
        pages = result['query']['pages']
        for key, args in pages.items():
            self.story = args['extract'], args['fullurl']

        return self.story