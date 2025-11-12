import heapq
from collections import defaultdict


def heappush_min(pq, tup):
    heapq.heappush(pq, tup)


def heappop_min(pq):
    return heapq.heappop(pq)


def heappush_max(pq, tup):
    heapq.heappush(pq, tuple(-item for item in tup))


def heappop_max(pq):
    tup = heapq.heappop(pq)
    return tuple(-item for item in tup)


class Set:
    def __init__(self):
        self._dict = {}
        self._dict_keys_min_pq = []
        self._dict_keys_max_pq = []
        self._sum = 0

    def add(self, occurrence: int, num: int):
        self._dict[(occurrence, num)] = None
        heappush_min(self._dict_keys_min_pq, (occurrence, num))
        heappush_max(self._dict_keys_max_pq, (occurrence, num))
        self._sum += occurrence * num

    def remove(self, occurrence: int, num: int) -> bool:
        try:
            del self._dict[(occurrence, num)]
            self._sum -= occurrence * num
            return True
        except KeyError:
            return False

    def __len__(self) -> int:
        return self._dict.__len__()

    def min(self):
        while True:
            key = heappop_min(self._dict_keys_min_pq)
            if key in self._dict:
                heappush_min(self._dict_keys_min_pq, key)
                return key

    def max(self):
        while True:
            key = heappop_max(self._dict_keys_max_pq)
            if key in self._dict:
                heappush_max(self._dict_keys_max_pq, key)
                return key

    def sum(self):
        return self._sum


class TopSum:
    def __init__(self, top_size: int):
        self._top_size = top_size
        self._occurrences = defaultdict(lambda: 0)

        self._top_set = Set()
        self._bot_set = Set()

    def remove(self, num: int):
        self._top_set.remove(self._occurrences[num], num)
        self._bot_set.remove(self._occurrences[num], num)
        self._occurrences[num] -= 1
        self._bot_set.add(self._occurrences[num], num)

    def add(self, num: int):
        self._top_set.remove(self._occurrences[num], num)
        self._bot_set.remove(self._occurrences[num], num)
        self._occurrences[num] += 1
        self._bot_set.add(self._occurrences[num], num)

    def sum(self) -> int:
        while len(self._bot_set) > 0 and len(self._top_set) < self._top_size:
            self._top_set.add(*self._bot_set.max())
            self._bot_set.remove(*self._bot_set.max())

        while (
            len(self._top_set) > 0
            and len(self._bot_set) > 0
            and self._bot_set.max() > self._top_set.min()
        ):
            self._bot_set.add(*self._top_set.min())
            self._top_set.remove(*self._top_set.min())

            self._top_set.add(*self._bot_set.max())
            self._bot_set.remove(*self._bot_set.max())

        return self._top_set.sum()


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        top_sum = TopSum(x)

        answers = []
        for i in range(len(nums)):
            if i >= k:
                top_sum.remove(nums[i - k])

            top_sum.add(nums[i])

            if i >= k - 1:
                ans = top_sum.sum()
                answers.append(ans)

        return answers
