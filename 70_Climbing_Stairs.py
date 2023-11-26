from typing import List


class Solution0:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]



if __name__ == '__main__':
    grids = [2, 3, 10]

    sols = [2, 3, 10]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(grids):
            if solution.climbStairs(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
