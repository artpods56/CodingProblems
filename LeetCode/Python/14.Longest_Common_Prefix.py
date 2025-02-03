#lc_14:03_02_2025
#https://leetcode.com/problems/longest-common-prefix/description/?source=submission-ac

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if [prefix] == strs:
            return prefix

        min_len = min([len(string) for string in strs])

        for i in range(min_len):
            if len(set([string[i] for string in strs])) == 1:
                prefix += strs[0][i]
            else:
                break

        return prefix
        
