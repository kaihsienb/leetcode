def score(num: int) -> int:
    return 1 if num % 2 == 0 else -1


class Solution:
    def maxBalancedSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        xor = [0]
        for i in range(n):
            xor.append(xor[-1] ^ nums[i])

        parity = [0]
        for i in range(n):
            parity.append(parity[-1] + score(nums[i]))

        d = {}
        for idx, (xor_v, parity_v) in enumerate(zip(xor, parity)):
            d[(xor_v, parity_v)] = idx

        ans = 0
        for i in range(n + 1):
            ans = max(ans, d[(xor[i], parity[i])] - i)

        return ans
