# lc_58:13_02_2025
# https://leetcode.com/problems/length-of-last-word/description/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = ""
        for i in range(len(s)):
            index = -(i + 1)
            if last_word == "" and s[index] == " ":
                continue
            elif last_word != "" and s[index] == " ":
                return len(last_word)
            else:
                last_word += s[index]
        return len(last_word)
