class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0

        return 1 + self.countOperations(min(num1, num2), abs(num1 - num2))
