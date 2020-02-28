from nose.tools import *
from ex48 import parser

def test_peek():
    assert_equal(parser.peek([['verb', 'go'], ['direction', 'north']]),'verb')

def test_match():
    assert_equal(parser.match([['verb', 'go'], ['direction', 'north']],'verb'),['verb','go'])

def test_skip():
    assert_equal(parser.skip([['verb', 'go'], ['direction', 'north']],'verb'),['verb','go'])

def test_parse_verb():
    assert_equal(parser.test_verb([['stop','the']],'stop'),)

