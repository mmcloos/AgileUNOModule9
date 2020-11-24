"""
Maggie Cloos
11-18-2020
My Module
"""

import json

def greeting(name):
    return(f"Hello {name}")

def letter_text(**kwargs):
    if "name" and "amount" and "denomination" in kwargs.keys():
        return(f"Hello {kwargs['name']}, this letter is to inform you that you have won {kwargs['amount']} {kwargs['denomination']},")
    else:
        return("incorrect parameters supplied")

my_json_data = {}

with open("input.json", "r") as input:
    my_json_data = json.load(input)
