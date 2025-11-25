class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        seen = set()

        n = 1
        n_len = 1
        add = 10 % k
        while n % k != 0:
            if (n, add) in seen:
                break

            seen.add((n, add))

            n = (n + add) % k
            n_len += 1
            add = (add * 10) % k
        else:
            return n_len

        return -1
