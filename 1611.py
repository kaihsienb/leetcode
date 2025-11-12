import functools


@functools.cache
def num_ops_to_zero(lg_n: int) -> int:
    if lg_n == 0:
        return 1

    return 2 * num_ops_to_zero(lg_n - 1) + 1


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0

        idx = 0
        while n > 0:
            if n % 2 == 1:
                ans = num_ops_to_zero(idx) - ans

            n //= 2
            idx += 1

        return abs(ans)
