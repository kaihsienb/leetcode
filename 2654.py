from math import gcd


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        nums_gcd = gcd(*nums)
        if nums_gcd > 1:
            return -1

        if ones := nums.count(1):
            return len(nums) - ones

        min_ops_for_one = len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if j - i >= min_ops_for_one:
                    break

                if gcd(*nums[i:j]) == 1:
                    min_ops_for_one = j - i

        return min_ops_for_one + len(nums) - 1
