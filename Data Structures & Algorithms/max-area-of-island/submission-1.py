class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        ans = 0

        def dfs(i,j):
            if not(0<=i<m) or not(0<=j<n) or grid[i][j] != 1: return 0
            grid[i][j] = 0
            return dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1) +1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i,j))
        return ans