# lc_3452:16_02_2025
# https://leetcode.com/problems/sum-of-good-numbers/description/


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        sum = 0

        for i, num in enumerate(nums):
            xk, yk = i - k, i + k
            index_range = range(len(nums))

            if xk in index_range and yk in index_range:
                if num > nums[xk] and num > nums[yk]:
                    sum += num

            elif xk in index_range and yk not in index_range:
                if num > nums[xk]:
                    sum += num

            elif yk in index_range and xk not in index_range:
                if num > nums[yk]:
                    sum += num
            else:
                sum += num

        return sum
