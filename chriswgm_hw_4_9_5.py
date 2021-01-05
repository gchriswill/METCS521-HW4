"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/04/2020
Homework Problem: #4.9.5
Description: A program to get the common letters from a string and creates and
prints an histogram.

"""

from collections import Counter

STR_ENG_SENTENCE = "WWAS IT A RAT I SAWW"
print("The string being analyzed is: {} ".format(STR_ENG_SENTENCE))

str_sentence_prep = STR_ENG_SENTENCE.replace(" ", "").lower()
common_t_list = Counter(str_sentence_prep).most_common()
dict_commons = dict(common_t_list)
print("Sorted dictionary of letter counts: {}".format(dict_commons))

max_l, max_f = max(Counter(str_sentence_prep).most_common())
common_max_t_list = [(l, f) for (l, f) in common_t_list if f == max_f]
str_most_common_letters = "{}".format([str(l) for (l, f) in common_max_t_list])
print("Most frequent letters {} appear {} times..."
      .format(str_most_common_letters, max_f))

common_letters_list = [str(str(k)[:]*int(v) + "\n") for k, v in dict_commons.items()]
print("Histogram: \n{}".format("".join(common_letters_list)))
