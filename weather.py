import csv
from datetime import datetime
from encodings import utf_8
import statistics
import pandas 
import os

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
    temp_c = round(((float(temp_in_farenheit) - 32) * 5 / 9),1) 
    return temp_c
print(convert_f_to_c(390))

weather_data = [35,6,14,26,9,1]

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

    weather_data = []

    with open(csv_file, encoding="utf-8") as csv_file: 
        file_reader = csv.reader(csv_file, delimiter = ",")
        next(file_reader)
        for line in file_reader: 
            if line:
                weather_data.append([line[0],float(line[1]),float((line[2]))])      
    return weather_data

print(load_data_from_csv("tests/data/example_one.csv"))    


weather_data = [49, 57, 56, 55, 53, 49]


def find_min(weather_data): #min max functions https://www.youtube.com/watch?v=fdwyp1xvD_I, range length https://www.freecodecamp.org/news/list-index-out-of-range-python-error-message-solved/#:~:text=You'll%20get%20the%20Indexerror,you're%20using%20negative%20indexing.
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if weather_data == []: #if list is empty
        return() #skip
    else: #if list has content
        min_val = float(weather_data[0]) #min value = typecasted first index of list
        for i in range(0,len(weather_data),1): #for weather temp in range to length of list
            if min_val >= float(weather_data[i]): #if min value greater than intital variable
                min_val = min(min_val, float(weather_data[i])) #min function used to declare the min value in the list
                min_index = i #min index equals index
    return min_val, min_index
    
print(find_min(weather_data))

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []: #if list is empty
        return() #skip
    else: #if list has content
        max_val = float(weather_data[0]) #min value = typecasted first index of list
        for i in range(0,len(weather_data),1): #for weather temp in range to length of list
            if max_val <= float(weather_data[i]): #if max value less than initial variable
                max_val = max(max_val, float(weather_data[i])) #max function used to declare the max value in the list
                max_index = i #min index equals index
    return max_val, max_index

print(find_max(weather_data))

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # weather_data = load_data_from_csv("tests/data/example_two.csv")
    days = len(weather_data)
    lowest_record = [min[1] for min in weather_data] #retreiving the lowest temp in list https://www.delftstack.com/howto/python/one-line-for-loop-python/
    highest_record = [max[2] for max in weather_data] #retreiving the highest temp in list
    dates = [date[0] for date in weather_data] #retreiving the date index

    lowest_temp =  format_temperature(convert_f_to_c(find_min(lowest_record)[0])) #3 functions to find from the lowest_record in list
    highest_temp = format_temperature(convert_f_to_c(find_max(highest_record)[0]))
    lowest_date = convert_date(dates[find_min(lowest_record)[1]])
    highest_date = convert_date(dates[find_max(highest_record)[1]])

    avg_low = format_temperature(convert_f_to_c(calculate_mean(lowest_record)))
    avg_high = format_temperature(convert_f_to_c(calculate_mean(highest_record)))

    # print(f" lowest_temp: {lowest_temp}")
    # print(f" highest_temp: {highest_temp}")
    # print(f" avg low: {avg_low}")
    # print(f" avg high: {avg_high}")

    return f"{days} Day Overview\n  The lowest temperature will be {lowest_temp}, and will occur on {lowest_date}.\n  The highest temperature will be {highest_temp}, and will occur on {highest_date}.\n  The average low this week is {avg_low}.\n  The average high this week is {avg_high}.\n"

# print(generate_summary(weather_data))

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
weather_data = load_data_from_csv("tests/data/example_two.csv")
daily_list = []


for data in weather_data:
    day = data[0]
    # max_temp = format_temperature(convert_f_to_c(find_max(weather_data[0][2])))
    lowest_record = [min[1] for min in weather_data]

print(lowest_record)

# ---- Friday 02 July 2021 ----
#   Minimum Temperature: 9.4°C
#   Maximum Temperature: 19.4°C

# ---- Saturday 03 July 2021 ----
#   Minimum Temperature: 13.9°C
#   Maximum Temperature: 20.0°C

# ---- Sunday 04 July 2021 ----
#   Minimum Temperature: 13.3°C
#   Maximum Temperature: 16.7°C

# ---- Monday 05 July 2021 ----
#   Minimum Temperature: 12.8°C
#   Maximum Temperature: 16.1°C

# ---- Tuesday 06 July 2021 ----
#   Minimum Temperature: 11.7°C
#   Maximum Temperature: 16.7°C
