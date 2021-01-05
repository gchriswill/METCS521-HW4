"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/04/2020
Homework Problem: #4.9.4
Description: A program that grabs a dictionary and prints its keys, its values
and its key/values (in order by key and in order by value).

"""


# Importing operator library for `itemgetter` convenience function
import operator


# A dictionary of strings as keys and integers as values
my_dict = {"a": 15, "c": 18, "b": 20}

# A my_dict dictionary sorted in ascending order by key
my_dict_sorted_key = dict(sorted(my_dict.items(), key=operator.itemgetter(0)))

# A my_dict dictionary sorted in descending order by value
my_dict_sorted_value = dict(sorted(my_dict.items(),
                                   key=operator.itemgetter(1), reverse=True))

# Printing all keys from my_dict dictionary
print("Keys: {}".format(list(my_dict.keys())))

# Printing all values from my_dict dictionary
print("values: {}".format(list(my_dict.values())))

# Printing all key/values pairs from my_dict dictionary
print("Key value pairs: {}".format(my_dict).replace("{", "").replace("}", ""))

# Printing all key/values pairs in order of key from my_dict dictionary
print("Key value pairs in order of key: {}".format(my_dict_sorted_key))

# Printing all key/values pairs in order of value from my_dict dictionary
print("Key value pairs in order of value: {}".format(my_dict_sorted_value))
