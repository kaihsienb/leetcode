def decimal_to_base_9(decimal):
    if decimal == 0:
        return 0

    remainder = decimal % 9
    if remainder == 0:
        return decimal_to_base_9(decimal // 9 - 1) * 10 + 9

    return decimal_to_base_9(decimal // 9) * 10 + (decimal % 9)


class Solution:
    def countDistinct(self, n: int) -> int:
        ans = 0

        lo, hi = 1, n + 1
        while lo < hi:
            mid = (lo + hi) // 2

            if decimal_to_base_9(mid) <= n:
                ans = mid
                lo = mid + 1
            else:
                hi = mid

        return ans
