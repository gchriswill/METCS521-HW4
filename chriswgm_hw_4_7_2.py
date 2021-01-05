"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/04/2020
Homework Problem: #4.7.2
Description: A program that takes a list of integers, creates and prints a new
list with the each item as the sum of the original plus its nearest neighbors.

"""

# A constant list of integers
INT_LIST = [10, 20, 30, 40, 50]

# Printing the list of integers
print("Input List: {}".format(INT_LIST))

# Printing the list of integers with the sum of its nearest neighbors
# Using comprehension list statements (left side + current + right side)
# Works with any range of numbers. Even with negatives!
print("Result List: {}".format([sum(INT_LIST[i if i <= 0 else i-1:i+2:1])
                                for i, e in enumerate(INT_LIST)]))
