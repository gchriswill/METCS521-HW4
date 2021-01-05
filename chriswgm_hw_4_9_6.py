"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/04/2020
Homework Problem: #4.9.6
Description:

Chapter 9 Exercises
4.9.6: Create a program that:
X prompts a user for a number
X validates the number
• re-prompts on error
• converts the number to words using a dictionary
• prints out the converted numbers as words

The program must only have one input command and work for any size positive or
negative number. Decimal point should be converted to ‘point’. If the user
enters commas, tell them to try again without the commas.

Example Output #1
Enter a number: 123
As Text: One Two Three

Example Output #2
Enter a number: -123
As Text: Negative One Two Three

Example Output #3
Enter a number: 1234.76
As Text: One Two Three Four Point Seven Six

Example Output #4 – invalid Input
Enter a number: 1,000
Please try again without entering commas.

Enter a number: 1 thousand
"1 thousand" is not a valid number. Please try again Enter a number: 1000.00
As Text: One Zero Zero Zero Point Zero Zero

"""

# DID NOT FINISHED...
# I started to work on it too late and prefer to deliver early than late
# I apologize...

WORDS_INTS = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
              "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

str_input = input("Enter a number: ")


def comma_checker(input_param):

    if str(input_param).__contains__(","):
        print("Please try again without entering commas.")
        return False
    else:
        return True


def int_check(input_param):

    if str(input_param).isnumeric() or str(input_param).isdecimal():
        return True
    else:
        print("Please try again by entering a number.")
        return False
