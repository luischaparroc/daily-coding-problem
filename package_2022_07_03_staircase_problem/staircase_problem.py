from typing import Set


def number_ways_optimized(n: int, allowed_steps: Set = {1, 2}):
    if n == 0:
        return 1

    nums = [0 for _ in range(n + 1)]
    nums[0] = 1

    for i in range(1, n + 1):
        total = 0
        for allowed_step in allowed_steps:
            if i - allowed_step >= 0:
                total += nums[i - allowed_step]
        nums[i] = total

    return nums[n]
