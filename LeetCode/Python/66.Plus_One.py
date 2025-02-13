# lc_66:13_02_2025
# https://leetcode.com/problems/plus-one/description/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits)):
            index = -(i + 1)
            if digits[index] == 10:
                digits[index] = 0
                if i + 1 == len(digits):
                    digits.insert(1, 0)
                digits[index - 1] += 1
            else:
                return digits
        return digits
