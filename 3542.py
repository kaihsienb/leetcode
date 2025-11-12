class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        stack = [0]
        for num in nums:
            while num < stack[-1]:
                stack.pop()

            if num > stack[-1]:
                stack.append(num)
                ans += 1

        return ans
