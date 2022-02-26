import numpy as np
import json
import requests

def roman_numeral(x):
    tracker = x
    
    if (tracker >= 100):
        return "C" + roman_numeral(tracker-100)
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
    
    return ""
d = dict()
i = 255
#for i in range(120):
#    d["input"] = str(i)
#    d["output"] = ruman_numeral(i)

d =   {
    "input" : str(i),
    "output" : roman_numeral(i)  
    }

json_string = json.dumps(d)
with open('output_file.json', 'w') as output_file:
    print("The json file is created")
    output_file.write(json_string)
    
