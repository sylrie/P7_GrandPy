"""Manage Granpy responses"""

#! /usr/bin/env python3
# coding: UTF-8

from random import choice

class Grandpy():
    """ grandpy responses"""

    def __init__(self, status, response):

        self.status = status

        self.grandpy_1 = ""
        self.grandpy_2 = ""

        if response == 1:
            self.grandpy_response_1()
        else:
            self.grandpy_response_2()

    def grandpy_response_1(self):
        """ choose the first grandpy response"""

        if self.status != "OK":

            self.grandpy_1 = choice(
                [
                    "Ah non mon poussin, là je ne vois pas de quoi tu parles !",
                    "Tu peux répéter en articulant ?",
                    "Je ne connais pas ce lieu, il ne doit pas exister !"
                ]
            )

        else:
            self.grandpy_1 = choice(
                [
                    "J'ai bien trouvé le lieu que tu cherchais, l'adresse est : ",
                    "Oui mon poussin, je connais ! L'adresse c'est : ",
                    "Effectivement mon petit, c'est ici : "
                ]
            )

        return self.grandpy_1

    def grandpy_response_2(self):
        """ choose the second grandpy response"""
        if self.status != "":

            self.grandpy_2 = choice(
                [
                    "Je connais bien ce quartier !",
                    "Mais t'ai-je déjà raconté l'histoire de ce quartier qui "
                    "m'a vu en culottes courtes ? ",
                    "Je pourrais t'en raconter de belles sur ce coin, par exemple. "
                ]
            )

        else:
            self.grandpy_2 = choice(
                [
                    "C'est rare mais là, j'ai rien à ajouter",
                    "Je connais bien ce quartier, mais j'ai pas envie d'en parler"
                ]
            )
