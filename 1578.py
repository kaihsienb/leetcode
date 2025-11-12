class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_cost = 0

        last_idx = None
        for idx, (color, cost) in enumerate(zip(colors, neededTime)):
            if last_idx is None or colors[last_idx] != color:
                last_idx = idx
                continue

            if neededTime[last_idx] < neededTime[idx]:
                total_cost += neededTime[last_idx]
                last_idx = idx
            else:
                total_cost += neededTime[idx]

        return total_cost
