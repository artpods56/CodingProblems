# lc_35:09_02_2025
# https://leetcode.com/problems/search-insert-position/description/


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        i = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
