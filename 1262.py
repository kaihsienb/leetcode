def max_(x: int | None, y: int | None) -> int | None:
    if x is None:
        return y

    if y is None:
        return x

    return max(x, y)


class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        dp = {}

        def solve(idx: int, modulo: int) -> int | None:
            if idx == 0:
                if nums[idx] % 3 == modulo:
                    return nums[idx]
                if modulo == 0:
                    return 0
                return None

            if (idx, modulo) in dp:
                return dp[(idx, modulo)]

            ans = solve(idx - 1, modulo)
            match nums[idx] % 3:
                case 0:
                    if (sub := solve(idx - 1, modulo)) is not None:
                        ans = max_(ans, sub + nums[idx])
                case 1:
                    if (sub := solve(idx - 1, (modulo + 2) % 3)) is not None:
                        ans = max_(ans, sub + nums[idx])
                case 2:
                    if (sub := solve(idx - 1, (modulo + 1) % 3)) is not None:
                        ans = max_(ans, sub + nums[idx])

            dp[(idx, modulo)] = ans
            return ans

        return solve(len(nums) - 1, 0)
