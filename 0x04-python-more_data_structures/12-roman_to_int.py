def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    prev_value = 0
    total = 0
    
    for symbol in reversed(roman_string):
        value = roman_numerals[symbol]
        
        if value >= prev_value:
            total += value
        else:
            total -= value
        
        prev_value = value
    
    return total

# Test cases
print(roman_to_int("III"))  # Output: 3
print(roman_to_int("IV"))   # Output: 4
print(roman_to_int("IX"))   # Output: 9
print(roman_to_int("LVIII")) # Output: 58
print(roman_to_int("MCMXCIV")) # Output: 1994
print(roman_to_int(None))   # Output: 0
print(roman_to_int("ABC"))  # Output: 0
