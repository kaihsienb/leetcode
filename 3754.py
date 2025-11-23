class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10

        digits = list(reversed(digits))

        x = 0
        for digit in digits:
            if digit != 0:
                x = x * 10 + digit

        return x * sum(digits)
