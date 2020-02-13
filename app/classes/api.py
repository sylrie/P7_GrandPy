""" Use GooGleMpas API (Geocode) and MediaWiki API"""

#! /usr/bin/env python3
# coding: UTF-8
import os
from requests import get

class GmapsRequest():
    """ Use GoogleMaps API (geocode) for find the adress"""

    def __init__(self, user_request):

        self.api_key = os.getenv("API_KEY_server")
        self.user_request = user_request
        self.data = {}

        self.request_api()

    def request_api(self):
        """ GoogleMaps API request
        get status, lat, lng and address"""

        url = "https://maps.googleapis.com/maps/api/geocode/json"

        params = {
            'address': self.user_request,
            'key': self.api_key,
            'region':'fr'
        }

        request = get(url=url, params=params)
        result = request.json()

        if result['status'] == "OK":
            self.data = {
                "status": "OK",
                "lat": result['results'][0]['geometry']['location']['lat'],
                "lng": result['results'][0]['geometry']['location']['lng'],
                "address": result['results'][0]['formatted_address']
            }

        else:
            self.data = {
                "status": result['status']
            }

        return self.data

class MediawikiRequest():
    """ use MediaWiki API for find a story"""

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.story = ""
        self.request_api()

    def request_api(self):
        """ MediaWiki API request
        get story and url"""

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
        try:
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
        except:
            pass

        return self.story

