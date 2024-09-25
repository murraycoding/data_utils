""" Functions to extract, format or transform dates """
### IMPORTS ###
from datetime import date, datetime
import re

### FUNCTION DEFINITIONS ###
def format_date(month, day, year = None):
    """
    Returns the date as a date object regardless of the input
    """

    # establishes current year
    try:
        if year is None:
            now = datetime.now()
            year = now.year

        int_year = int(year)
    except ValueError as value_error:
        print(f"Error: Cannot convert year to a integer. ERROR = {value_error}")
        raise value_error
    except Exception as error:
        print(f"Unknown exception occured. ERROR = {error}")
        raise error

    if len(str(year)) == 2:
        int_year = int(year) + 2000

    if int_year < 2000 or int_year > 2100:
        print("Year is out of range.")
        return False

    try:
        int_month = int(month)
        int_day = int(day)
        date_obj = date(int_year, int_month, int_day)
    except ValueError as value_error:
        print(f"Could not convert month or day to integers. ERROR = {value_error}")
        raise value_error

    return date_obj

def pull_date_from_filename(file_name:str):
    """
    Input: filename as string
    Output: Date object made with the format_date function
    """
    # type checking
    if not isinstance(file_name, str):
        print("The function pull_date_from_filename requires a string input")
        raise TypeError
    
    # pattern matching
    long_date_pattern = r"\d{2,4}\W\d{2,4}\W\d{2,4}"
    long_date_results = re.search(file_name, long_date_pattern)

    short_date_pattern = r"\d{2,4}\W\d{2,4}"
    short_date_results = re.search(file_name, short_date_pattern)

    


