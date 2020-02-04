#! /usr/bin/env python3
# coding: UTF-8

from requests import get
from killerparser import Parser
from api import GmapsRequest, MediawikiRequest
from grandpy import Grandpy


class UserRequest:

    def __init__(self, sentence):

        self.sentence = sentence
        self.grandpy_number = int
        
        self.location = {
            "lat" : "",
            "lng" : ""
        }

        self.response = {
            "papy_1" : "",
            "address" : "",
            "papy_2" :"",
            "story" : "",
            "fullurl" : ""
        }
        self.location_status = ""

        self.run_search()

    def run_search(self):

        self.parse_sentence()
        self.get_location()
        if self.location_status == "OK":
            self.get_story()
        else:
            pass

        return self.response

    def parse_sentence(self):

        self.sentence = Parser(self.sentence).sentence

    def get_location(self):

        self.grandpy_number = 1
        loc = GmapsRequest(self.sentence)

        self.location_status = loc.data.get("status")

        papy = Grandpy(self.location_status, self.grandpy_number)

        if self.location_status == "OK":
            self.location["lat"] = loc.data.get("lat")
            self.location["lng"] = loc.data.get("lng")
            self.response["address"] = loc.data.get("address")
            self.response["papy_1"] = papy.grandpy_1
            
        else:
            self.response["papy_1"] = papy.grandpy_1
            
    def get_story(self):

        self.grandpy_number = 2

        story = MediawikiRequest(self.location['lat'],self.location['lng'])
        status = ""
        if story.story[0] != "":
            status = "OK"
            papy = Grandpy(status, self.grandpy_number)

            self.response["papy_2"] = papy.grandpy_2
            self.response["story"] = story.story[0]
            self.response["fullurl"] = story.story[1]
        else:
            papy = Grandpy(status, self.grandpy_number)

            self.response["papy_2"] = papy.grandpy_2

