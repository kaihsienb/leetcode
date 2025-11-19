class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        idx = 0
        while idx < len(bits):
            if bits[idx] == 0:
                idx += 1
                if idx == len(bits):
                    return True
            else:
                idx += 2

        return False
