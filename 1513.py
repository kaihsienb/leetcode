class Solution:
    def numSub(self, s: str) -> int:
        ones = [0]
        for c in s:
            if c == "0":
                ones.append(0)
            else:
                ones[-1] += 1

        return sum(map(lambda x: x * (x + 1) // 2, ones)) % 1000000007
