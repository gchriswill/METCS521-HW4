"""
Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/04/2020
Homework Problem: #4.7.1
Description: A program for evaluating and filtering a list of integers by Even
and Odd numbers, and printing these to the console.

"""


# A constant list of integers
INT_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Printing the complete list of integers
print("Evaluating the numbers in: {}".format(INT_LIST))

# Printing a list of integers manually filtered by Even numbers
print("Even: {}".format([int(i) for i in INT_LIST if int(i) % 2 == 0]))

# Printing a list of integers manually filtered by Odd numbers
print("Odd: {}".format([int(i) for i in INT_LIST if int(i) % 2 != 0]))

