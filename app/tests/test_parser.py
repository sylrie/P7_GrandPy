#! /usr/bin/env python3
# coding: UTF-8


from ..classes.killerparser import Parser


def test_parser():
    parser = Parser("Salut GrandPy ! Est-ce que tu connais l'adresse d'openclassrooms ?")
    test_result = "openclassrooms"
    assert parser.sentence == test_result

def test_parser_empty():
    parser = Parser("")
    test_result = ""
    assert parser.sentence == test_result