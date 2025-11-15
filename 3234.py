def ones_needed(zeros: int) -> int:
    return zeros * zeros


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        next_zero_from = [n for _ in range(n + 1)]
        for i in reversed(range(n)):
            next_zero_from[i] = i if s[i] == "0" else next_zero_from[i + 1]

        ans = 0
        for i in range(n):
            next_zero_pos = next_zero_from[i]

            zeros = 0
            ones = next_zero_pos - i
            ans += ones

            while next_zero_pos < n:
                curr_zero_pos = next_zero_pos
                next_zero_pos = next_zero_from[curr_zero_pos + 1]

                zeros += 1
                new_ones = next_zero_pos - curr_zero_pos - 1
                ones += new_ones

                ans += max(0, min(new_ones + 1, ones - ones_needed(zeros) + 1))

                if ones_needed(zeros) > n - i - zeros:
                    break

        return ans
