#lc_20:04_02_2024
#https://leetcode.com/problems/valid-parentheses/description/#

class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        mapped = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        if s[0] in mapped.keys() or len(s) % 2 != 0:
            return False

        for i in range(len(s)):
            if s[i] in mapped.values():
                opened.append(s[i])
            elif opened and opened.pop() == mapped[s[i]]:
                continue
            else:
                return False
            
        return not opened
