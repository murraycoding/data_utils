""" File for unit tests for code in date_utils.py """

### IMPORTS ###
import pytest

from date_utils import *


### UNIT TESTS ###

# format date tests
def test_format_date_with_integers():
    assert format_date(12,10) == date(2024,12,10)

def test_format_date_with_strings():
    assert format_date("12","10") == date(2024,12,10)

def test_format_date_value_error():
    with pytest.raises(ValueError):
        format_date("a","b")

def test_format_date_int_str_with_0_value():
    assert format_date("02","04") == date(2024,2,4)

def test_format_date_with_2digit_year():
    assert format_date("12","13","14") == date(2014,12,13)

def test_format_date_with_0n_year():
    assert format_date("12","13","04") == date(2004,12,13)

def test_format_date_with_four_digit_year():
    assert format_date(12,13,2024) == date(2024,12,13)
