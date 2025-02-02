#lc_13:02_02_2025
#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_digits_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        reversed_string = s[::-1]
        result = roman_digits_map[reversed_string[0]]
        
        for i in range(1,len(reversed_string)):
            first_number = roman_digits_map[reversed_string[i]]
            second_number = roman_digits_map[reversed_string[i-1]]
            
            if first_number >= second_number:
                result += first_number
            else:
                result -= first_number

        return result

