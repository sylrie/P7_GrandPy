#! /usr/bin/env python3
# coding: UTF-8


from ..parser import Parser


def test_lower_character():
    parser = Parser("Salut")
    test_result = "salut"
    assert parser.lower_character() == test_result
       