from typing import List


class Solution0:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in coins:
            return amount

        dp = [0] * (amount + 1)
        dp[0] = 0


if __name__ == '__main__':
    coins = [[1, 2, 5], [2], [1]]

    sols = [3, -1, 0]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(grids):
            if solution.climbStairs(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
