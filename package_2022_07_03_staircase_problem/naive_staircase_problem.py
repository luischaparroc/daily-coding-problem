from typing import Set


def number_ways(n: int, allowed_steps: Set = {1, 2}):

    if n == 0:
        return 1

    if n < 0:
        return 0

    n_ways = 0

    for allowed_step in allowed_steps:
        n_ways += number_ways(n - allowed_step, allowed_steps)

    return n_ways
