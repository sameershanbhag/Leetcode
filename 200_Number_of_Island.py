from typing import List


class Solution0:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return "0"

            if grid[i][j] == "0":
                return "0"

            grid[i][j] = "0"

            dfs(i + 1, j, grid)
            dfs(i - 1, j, grid)
            dfs(i, j + 1, grid)
            dfs(i, j - 1, grid)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c, grid)

        return count


if __name__ == '__main__':
    grids = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ],
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
    ]

    sols = [1, 3]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(grids):
            if solution.numIslands(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
