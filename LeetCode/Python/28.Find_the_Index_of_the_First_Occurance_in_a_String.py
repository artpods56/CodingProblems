# lc_28:05_02_2025
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, len(needle)
        while j <= len(haystack):
            if needle == haystack[i:j]:
                return i
            i += 1
            j += 1
        return -1
