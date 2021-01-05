"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/04/2020
Homework Problem: #4.9.3
Description: A program that grabs 2 lists, checks that these are of the same
size, generates a dictionary and prints it.

"""


# A constant list of strings with names
NAMES_LIST = ["Jane", "John", "Jack"]

# A constant list of strings with last names
LASTS_LIST = ["Doe", "Deer", "Black"]

# Checks that the lists are both the same size
if len(NAMES_LIST) == len(LASTS_LIST):

    # Generates a dictionary using zip,
    # with last names as keys and first names as values,
    # then prints it.
    print("First Names: {}".format(NAMES_LIST))
    print("Last Names: {}".format(LASTS_LIST))
    print("Name Dictionary: {}".format(dict(zip(LASTS_LIST, NAMES_LIST))))
else:

    # Exits with Error message if the lists are not the same size
    exit("Error Message: The list are not the same size...")
