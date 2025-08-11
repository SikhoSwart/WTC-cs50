from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

#test for greetings beginning with H/h
def test_forh():
    assert value("Hey") == 20
    assert value("hi") == 20

#greetings with no H or hello
def test_noh():
    assert value("Whaddup") == 100
    assert value("ciao") == 100

