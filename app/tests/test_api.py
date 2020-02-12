#! /usr/bin/env python3
# coding: UTF-8

from ..classes.api import GmapsRequest, MediawikiRequest

import urllib.request


def test_googlemaps_ok(monkeypatch):

    test_result = {
        'status': 'OK',
        'lat': 48.8748465,
        'lng': 2.3504873,
        'address': '7 Cité Paradis, 75010 Paris, France'
        }
    
    def mockreturn(request):
        return test_result

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert GmapsRequest('openclassrooms').data == test_result

def test_googlemaps_error(monkeypatch):

    test_result = {'status': 'INVALID_REQUEST'}
    
    def mockreturn(request):
        return test_result

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert GmapsRequest('').data == test_result

def test_mediawiki(monkeypatch):
    test_story = ("L'Hôtel Bourrienne (appelé aussi Hôtel de Bourrienne et Petit Hôtel "
            'Bourrienne) est un hôtel particulier du XVIIIe siècle situé au 58 rue '
            "d'Hauteville dans le 10e arrondissement de Paris. Propriété privée, il est "
            'classé au titre des monuments historiques depuis le 20 juin 1927.')
    test_url = 'https://fr.wikipedia.org/wiki/H%C3%B4tel_Bourrienne'
    
    test_result = test_story, test_url

    def mockreturn(request):
        return test_result

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert MediawikiRequest(48.8748465, 2.3504873).story == test_result