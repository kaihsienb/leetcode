class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        prev_one_pos = None
        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            if prev_one_pos is not None and i - prev_one_pos <= k:
                return False

            prev_one_pos = i

        return True
