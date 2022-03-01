import numpy as np
import json
import requests

def roman_numeral(x):
    tracker = x
    if (type(x) != type(5)): # eroor handling in case the input is not an integer
        return "TypeError: not an integer";
    elif (tracker >= 100): # this and below is built in descending order in order for us to handle only the largest possible number everytime
        return "C" + roman_numeral(tracker-100) # recursive call which adds the roman numeral to the output and reduces the input of the recursive call
    elif (tracker >= 90): 
        return "XC" + roman_numeral(tracker-90)
    elif (tracker >= 50):
        return "L" + roman_numeral(tracker-50)
    elif (tracker >= 40):
        return "XL" + roman_numeral(tracker-40)
    elif (tracker >= 10):
        return "X" + roman_numeral(tracker-10)
    elif (tracker >= 9):
        return "IX" + roman_numeral(tracker-9)
    elif (tracker >= 5):
        return "V" + roman_numeral(tracker-5)
    elif (tracker >= 4):
        return "IV" + roman_numeral(tracker-4)
    elif (tracker >= 1):
        return "I" + roman_numeral(tracker-1)
    
    return "" # the zero was not a properly defined number in the roman numeral system and anyway the range we are interested in is from 1


