#!/usr/bin/env python3

def best_sum(target_sum, numbers):
    memo = {}

    def helper(target_sum, numbers):
        if target_sum == 0:
            return []
        if target_sum in memo:
            return memo[target_sum]
        shortest_combination = None
        for num in numbers:
            remainder = target_sum - num
            if remainder >= 0:
                combination = helper(remainder, numbers)
                if combination is not None:
                    combination = combination + [num]
                    if shortest_combination is None or len(combination) < len(
                        shortest_combination
                    ):
                        shortest_combination = combination
        memo[target_sum] = shortest_combination
        return memo[target_sum]

    return helper(target_sum, numbers)


print(best_sum(7, [4, 5, 3, 7]))