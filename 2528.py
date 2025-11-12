from collections import defaultdict
from typing import Sequence


def find_additional_stations_required(
    stations: Sequence[int], minimum_power: int, r: int
) -> int:
    stations_by_city = defaultdict(lambda: 0)
    for i in range(len(stations)):
        stations_by_city[i] = stations[i]

    additional_stations = 0

    power = sum(stations[: r + 1])
    for i in range(len(stations)):
        if power < minimum_power:
            diff = minimum_power - power
            additional_stations += diff

            stations_by_city[i + r] += diff
            power += diff

        # prepare for next city
        power += stations_by_city[i + r + 1]
        power -= stations_by_city[i - r]

    return additional_stations


class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        max_min_power = 0

        lower_bound = 0
        upper_bound = 20000000000
        while lower_bound < upper_bound:
            minimum_power = (lower_bound + upper_bound) // 2
            additional_stations_required = find_additional_stations_required(
                stations, minimum_power, r
            )

            if additional_stations_required > k:
                upper_bound = minimum_power
            else:
                max_min_power = minimum_power
                lower_bound = minimum_power + 1

        return max_min_power
