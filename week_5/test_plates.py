from plates import is_valid

def test_strlen():
    assert is_valid("AAA225433") == False
    assert is_valid("A") == False

def test_beginalpha():
    assert is_valid("11233") == False
    assert is_valid("AAA233") == True

#test if vanity has no numbers in the middle
def test_endnum():
    assert is_valid("AA222A") == False
    assert is_valid("AAA333") == True

#test if first number is not 0
def test_firstnum():
    assert is_valid("AAA023") == False

#testing if vanity is alphanumeric
def test_alphanum():
    assert is_valid("AAA34!") == False

