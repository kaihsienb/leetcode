import heapq
from collections import defaultdict
from typing import Mapping


def heappush_max(pq, tup):
    heapq.heappush(pq, tuple(-item for item in tup))


def heappop_max(pq):
    tup = heapq.heappop(pq)
    return tuple(-item for item in tup)


def solve(occurences: Mapping[int, int], pq: list, x: int) -> int:
    selected = set()
    while pq and len(selected) < x:
        occurence, num = heappop_max(pq)
        if occurences[num] != occurence or num in selected:
            continue

        selected.add(num)

    for num in selected:
        heappush_max(pq, (occurences[num], num))

    return sum(occurences[num] * num for num in selected)


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        occurrences = defaultdict(lambda: 0)
        pq = []

        answers = []
        for i in range(len(nums)):
            if i >= k:
                occurrences[nums[i - k]] -= 1
                heappush_max(pq, (occurrences[nums[i - k]], nums[i - k]))

            occurrences[nums[i]] += 1
            heappush_max(pq, (occurrences[nums[i]], nums[i]))

            if i + 1 < k:
                continue

            answers.append(solve(occurrences, pq, x))

        return answers
