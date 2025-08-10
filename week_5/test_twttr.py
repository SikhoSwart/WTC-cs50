from twttr import shorten

def test_uppercase():
    assert shorten("PYTHON IS COOL") == "PYTHN S CL"

def test_lowercase():
    assert shorten("python is cool") == "pythn s cl"

def test_numbers():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("boo!") == "b!"

