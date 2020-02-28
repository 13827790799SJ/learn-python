from nose.tools import *
from ex48 import lexion

def test_directions():
    assert_equal(lexion.scan('north'),[['direction','north']])
    result=lexion.scan('north south east')
    assert_equal(result,[['direction','north'],['direction','south'],['direction','east']])

def test_verbs():
    assert_equal(lexion.scan('go'),[['verb','go']])
    result=lexion.scan('go kill eat')
    assert_equal(result,[['verb','go'],['verb','kill'],['verb','eat']])

def test_stops():
    assert_equal(lexion.scan('the'),[['stop','the']])
    result=lexion.scan('the in of')
    assert_equal(result,[['stop','the'],['stop','in'],['stop','of']])

def test_nouns():
    assert_equal(lexion.scan('bear'),[['noun','bear']])
    result=lexion.scan('bear princess')
    assert_equal(result,[['noun','bear'],['noun','princess']])

def test_number():
    assert_equal(lexion.scan('1234'),[['number','1234']])
    result=lexion.scan('3 91234')
    assert_equal(result,[['number','3'],['number','91234']])

def test_errors():
    assert_equal(lexion.scan('ASDFADFASDF'),[['error','ASDFADFASDF']])
    result=lexion.scan('bear IAS princess')
    assert_equal(result,[['noun','bear'],['error','IAS'],['noun','princess']])