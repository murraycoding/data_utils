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

# pull date from filename tests
def test_filename_date_type_check1():
    with pytest.raises(TypeError):
        pull_date_from_filename(24)

def test_filename_date_type_check2():
    with pytest.raises(TypeError):
        pull_date_from_filename({"Testing"})

def test_filename_date_type_check1():
    with pytest.raises(TypeError):
        pull_date_from_filename(["Testing"])

