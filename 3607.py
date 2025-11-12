import heapq
from collections import defaultdict


class Solution:
    def processQueries(
        self, c: int, connections: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        adj_list = defaultdict(list)
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)

        group_id_by_station: dict[int, int] = {}
        stations_by_group_id: dict[int, list] = defaultdict(list)

        def dfs(station: int, group_id: int):
            group_id_by_station[station] = group_id
            heapq.heappush(stations_by_group_id[group_id], station)

            for neighbor in adj_list[station]:
                if neighbor not in group_id_by_station:
                    dfs(neighbor, group_id)

        group_id = 1
        for station in range(1, c + 1):
            if station not in group_id_by_station:
                dfs(station, group_id)
                group_id += 1

        responses = []

        operation_status_by_station = defaultdict(lambda: True)
        for op, station in queries:
            match op:
                case 1:
                    if operation_status_by_station[station]:
                        responses.append(station)
                    else:
                        group_id = group_id_by_station[station]
                        stations = stations_by_group_id[group_id]
                        while stations:
                            min_station = heapq.heappop(stations)
                            if operation_status_by_station[min_station]:
                                heapq.heappush(stations, min_station)
                                responses.append(min_station)
                                break
                        else:
                            responses.append(-1)
                case 2:
                    operation_status_by_station[station] = False
                case _:
                    raise RuntimeError(f"Unknown operation {op}")

        return responses
