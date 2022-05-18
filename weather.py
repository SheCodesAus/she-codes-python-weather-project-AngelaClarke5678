import csv
from datetime import datetime
from encodings import utf_8
import statistics
import pandas 

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
  
#     df = pd.read_csv(csv_file, delimiter=',')
#     list_of_rows = [list(row) for row in df.values] I tried PANDAS and it failed so I went back to forloops
#     for line in list_of_rows:
#         list_of_rows = list(map(float,line[1]))

#     return csv_file
# print(load_data_from_csv("tests/data/example_one.csv"))    


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
    # for weather in weather_data:
    #     weather_list = []
    #     weather = float(weather)
    #     weather_list.append(weather) 
    #     list_min = min(weather_data)
    #     min_index = weather_data.index(list_min)
    #     find_min = print(f"{list_min}, {min_index}")
    # return find_min

   
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
    # if weather_data != []:
    #     for element in weather_data:
    #         element = float(element)
    #         min_val = weather_data[0]
    #         if element <= float(min_val):
    #             min_val = element
    #             min_loc = index
    #         index += 1
    # return min_val, min_loc




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
    pass
lowest_temp = min(weather_data[1])
highest_temp = find_max(weather_data)
convert_date(weather_data)

print(highest_temp)
print(lowest_temp)


print("5 Day Overview")
print(f"The lowest temperature will be {lowest_temp} , and will occur on ")


#5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
