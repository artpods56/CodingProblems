# lc_1790:05_02_2025
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        set_s1 = set(list(s1))
        set_s2 = set(list(s2))

        differences = [s_1 == s_2 for s_1, s_2 in zip(s1, s2)]
        diff_count = differences.count(False)
        pointer = 0
        indexes = []
        for i in range(diff_count):
            pointer = differences.index(False, pointer)
            indexes.append(pointer)
            pointer += 1

        if s1 == s2:
            return True
        if len(indexes) != 2:
            return False

        x1, x2 = indexes
        s1[x1], s1[x2] = s1[x2], s1[x1]

        if s1 == s2:
            return True
        print(s1, s2)
        print(indexes)
        if set_s1.difference(set_s2) == set() and diff_count <= 2:
            if s1 == s2:
                return True
            else:
                return False
        else:
            return False
