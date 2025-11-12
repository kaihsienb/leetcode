class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        memo = {}

        def solve(idx: int, m: int, n: int) -> int:
            if idx == len(strs):
                return 0

            if m < 0 or n < 0:
                raise RuntimeError(f"{m=} {n=} cannot be less than zero!")

            if (idx, m, n) in memo:
                return memo[(idx, m, n)]

            ans = solve(idx + 1, m, n)

            zeros, ones = strs[idx].count("0"), strs[idx].count("1")
            if zeros <= m and ones <= n:
                ans = max(ans, 1 + solve(idx + 1, m - zeros, n - ones))

            memo[(idx, m, n)] = ans
            return ans

        return solve(0, m, n)
