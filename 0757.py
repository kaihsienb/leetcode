class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[1])

        nums = []
        for s, e in sorted_intervals:
            if not nums or nums[-1] < s:
                nums.append(e - 1)
                nums.append(e)
            elif nums[-2] < s:
                if nums[-1] == e:
                    nums.pop()
                    nums.append(e - 1)
                    nums.append(e)
                else:  # nums[-1] < e
                    nums.append(e)

        return len(nums)
