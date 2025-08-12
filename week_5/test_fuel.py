from fuel import convert, gauge
import pytest

def test_zerodiv():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_incorrectxy():
    with pytest.raises(ValueError):
        convert("two/four")
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("1.5/4")

def test_perc():
   assert convert("1/2") == 50

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"`
