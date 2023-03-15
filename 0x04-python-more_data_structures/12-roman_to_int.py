#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    value = 0
    for num in range(len(roman_string)):
        if num < len(roman_string) - 1:
            if rom_num[roman_string[num]] < rom_num[roman_string[num + 1]]:
                value -= rom_num[roman_string[num]]
            else:
                value += rom_num[roman_string[num]]
    return value
