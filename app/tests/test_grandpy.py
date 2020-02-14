""" Manage tests for Grandpy"""

#! /usr/bin/env python3
# coding: UTF-8

from ..classes.grandpy import Grandpy

def test_grandpy1_ok():
    granpy = Grandpy("OK", 1)
    test_result = [
                    "J'ai bien trouvé le lieu que tu cherchais, l'adresse est : ",
                    "Oui mon poussin, je connais ! L'adresse c'est : ",
                    "Effectivement mon petit, c'est ici : "
                ]
        
    assert granpy.grandpy_1 in test_result

def test_grandpy1_error():
    granpy = Grandpy("", 1)
    test_result = [
                    "Ah non mon poussin, là je ne vois pas de quoi tu parles !",
                    "Tu peux répéter en articulant ?",
                    "Je ne connais pas ce lieu, il ne doit pas exister !"
                ]
        
    assert granpy.grandpy_1 in test_result

def test_grandpy2_ok():
    granpy = Grandpy(" ", 2)
    test_result = [
                    "Je connais bien ce quartier !",
                    "Mais t'ai-je déjà raconté l'histoire de ce quartier qui "
                    "m'a vu en culottes courtes ? ",
                    "Je pourrais t'en raconter de belles sur ce coin, par exemple. "
                ]
        
    assert granpy.grandpy_2 in test_result

def test_grandpy2_error():
    granpy = Grandpy("", 2)
    test_result = [
                    "C'est rare mais là, j'ai rien à ajouter",
                    "Je connais bien ce quartier, mais j'ai pas envie d'en parler"
                ]
        
    assert granpy.grandpy_2 in test_result


