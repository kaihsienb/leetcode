from enum import Enum


class State(Enum):
    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3


def north_generator(m: int, n: int):
    for j in range(n):
        for i in range(m - 1, -1, -1):
            yield (i, j, i == m - 1)


def east_generator(m: int, n: int):
    for i in range(m):
        for j in range(n):
            yield (i, j, j == 0)


def south_generator(m: int, n: int):
    for j in range(n):
        for i in range(m):
            yield (i, j, i == 0)


def west_generator(m: int, n: int):
    for i in range(m):
        for j in range(n - 1, -1, -1):
            yield (i, j, j == n - 1)


class Solution:
    def countUnguarded(
        self,
        m: int,
        n: int,
        guards: list[list[int]],
        walls: list[list[int]],
    ) -> int:
        grid = [[State.UNGUARDED for _ in range(n)] for _ in range(m)]
        for [i, j] in guards:
            grid[i][j] = State.GUARD
        for [i, j] in walls:
            grid[i][j] = State.WALL

        for generator in [
            north_generator(m, n),
            east_generator(m, n),
            south_generator(m, n),
            west_generator(m, n),
        ]:
            state = State.UNGUARDED
            for i, j, reset_rowcol in generator:
                if reset_rowcol:
                    state = State.UNGUARDED

                if grid[i][j] == State.GUARD:
                    state = State.GUARDED
                if grid[i][j] == State.WALL:
                    state = State.UNGUARDED
                if grid[i][j] == State.UNGUARDED:
                    grid[i][j] = state

        return sum(grid[i].count(State.UNGUARDED) for i in range(m))
