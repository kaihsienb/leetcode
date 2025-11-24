class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans = []

        num = 0
        for i in range(len(nums)):
            num = (num * 2 + nums[i]) % 5

            ans.append(num % 5 == 0)

        return ans
