# lc_3:16_02_2025
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        i = 0
        longest = 0

        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1

            char_set.add(s[j])
            substring_len = j - i + 1

            if substring_len > longest:
                longest = substring_len

        return longest
