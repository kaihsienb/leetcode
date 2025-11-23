class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return sum(1 for num in nums if num % 3 != 0)
