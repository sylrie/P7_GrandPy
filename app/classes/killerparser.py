""" Parse the user request"""
#! /usr/bin/env python3
# coding: UTF-8

import json
import unicodedata

class Parser():
    """ Parse the user request using 'parsing_words.json' """

    def __init__(self, sentence):
        """ load parsing_words.json """

        self.sentence = sentence

        with open("app/docs/parsing_words.json", "r") as stopwords:
            parsing_words = json.load(stopwords)

        self.punctuation = parsing_words["punctuation"]
        self.stopwords = parsing_words["stopwords"]
        self.specialwords = parsing_words["specialwords"]

        self.parsing()

    def parsing(self):
        """ clean the sentence """

        self.lower_character()
        self.remove_accents()
        self.remove_punctuation()
        self.remove_stopwords()
        self.remove_specialwords()
        self.format_for_request()

    def lower_character(self):
        """ lower character """

        self.sentence = self.sentence.lower()
        return self.sentence

    def remove_accents(self):
        """ remove all accents """

        self.sentence = "".join(
            c for c in unicodedata.normalize('NFD', self.sentence)
            if unicodedata.category(c) != 'Mn'
            )
        return self.sentence

    def remove_punctuation(self):
        """ remove all punctuation """

        self.sentence = "".join(
            character for character in self.sentence if character not in self.punctuation
            )
        self.sentence = self.sentence.replace("'", " ")
        self.sentence = self.sentence.replace("-", " ")

        return self.sentence

    def remove_stopwords(self):
        """ clean the sentence removing stopwords """
        self.sentence = " ".join(
            word for word in self.sentence.split(" ") if word not in self.stopwords
            )
        return self.sentence

    def remove_specialwords(self):
        """ clean the sentence removing specialwords """

        self.sentence = " ".join(
            word for word in self.sentence.split(" ") if word not in self.specialwords
            )
        return self.sentence

    def format_for_request(self):
        """ set format for request api"""

        self.sentence = " ".join(self.sentence.split())
        self.sentence = self.sentence.replace(" ", "%20")
        return self.sentence
