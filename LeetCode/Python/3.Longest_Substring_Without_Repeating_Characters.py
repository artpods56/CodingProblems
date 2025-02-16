# lc_3:16_02_2025
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        j = 0
        longest = 0
        temp = ""

        while j < len(s):
            if s[j] not in temp:
                temp += s[j]
            else:
                temp = s[s.rindex(s[j], 0, j) : j]

            if len(temp) > longest:
                longest = len(temp)
            j += 1

        return longest
