# lc_1790:05_02_2025
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = [
            i for i, (char_1, char_2) in enumerate(zip(s1, s2)) if char_1 != char_2
        ]
        if len(diffs) == 0:
            return True
        elif len(diffs) == 2:
            x1, x2 = diffs
            s1, s2 = list(s1), list(s2)
            s1[x1], s1[x2] = s1[x2], s1[x1]
            if s1 == s2:
                return True
            else:
                return False
        else:
            return False
