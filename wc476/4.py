class Solution:
    def countStableSubarrays(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        n = len(nums)
        stable_length = [1]
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                stable_length.append(1)
            else:
                stable_length.append(stable_length[i - 1] + 1)

        max_stable_length = [stable_length[-1] for _ in range(n)]
        for i in reversed(range(n - 1)):
            if nums[i] > nums[i + 1]:
                max_stable_length[i] = stable_length[i]
            else:
                max_stable_length[i] = max_stable_length[i + 1]

        stable_subarrays_count = [1 for _ in range(n)]
        for i in range(1, n):
            stable_subarrays_count[i] = stable_subarrays_count[i - 1] + stable_length[i]

        ans_list = []
        for left, right in queries:
            left_diff = min(right - left, max_stable_length[left] - stable_length[left])
            ans = (
                stable_subarrays_count[right]
                - stable_subarrays_count[left + left_diff]
                + (left_diff + 1) * (left_diff + 2) // 2
            )

            ans_list.append(ans)

        return ans_list
