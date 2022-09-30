#!/usr/bin/python3
def roman_to_int(roman_string):
    tointeger = 0
    previous = 4000
    subtract = 0
    roman_numeral = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
            }
    if (isinstance(roman_string, int)):
        return 0
    if roman_string:
        for i in roman_string:
            if previous < roman_numeral[i]:
                subtract = roman_numeral[i] - previous
                tointeger -= previous
                tointeger += subtract
                previous = roman_numeral[i]
            else:
                tointeger += roman_numeral[i]
                previous = roman_numeral[i]
        return tointeger
    return 0
