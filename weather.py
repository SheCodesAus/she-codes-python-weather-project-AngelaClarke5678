import csv
from datetime import datetime
from encodings import utf_8
import statistics
import pandas as pd


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"
print(format_temperature("32"))

def convert_date(iso_string): #https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    convert_date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z") #creating the date time object
    convert_date =  datetime.strftime(convert_date, "%A %d %B %Y") #formating to required format
    return convert_date   
print(convert_date("2021-07-05T07:00:00+08:00"))


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_c = round(((float(temp_in_farenheit) - 32) * 5 / 9),1) #doing everything at once because I'm lazy
    return temp_c
print(convert_f_to_c(390))


weather_data = [5,9,32,27,56]
def calculate_mean(weather_data): #https://appdividend.com/2022/01/19/python-mean/
    weather_list = []
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    for weather in weather_data:
        weather = float(weather)
        weather_list.append(weather) 
        calculate_mean = statistics.mean(weather_list)
    return calculate_mean
print(calculate_mean(weather_data))

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
  
    df = pd.read_csv(csv_file, delimiter=',')
    list_of_rows = [list(row) for row in df.values]
    print(list_of_rows)
    return csv_file

print(load_data_from_csv("tests/data/example_one.csv"))    



def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
