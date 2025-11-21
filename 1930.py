from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        palindromes = set()

        l_set = set()
        r_set = set(s)
        r_counter = defaultdict(lambda: 0)
        for c in s:
            r_counter[c] += 1

        for c in s:
            r_counter[c] -= 1
            if r_counter[c] == 0:
                r_set.remove(c)

            intersects = l_set.intersection(r_set)
            for intersect in intersects:
                palindrome = f"{intersect}{c}{intersect}"
                palindromes.add(palindrome)

            l_set.add(c)

        return len(palindromes)
