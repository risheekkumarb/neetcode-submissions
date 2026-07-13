class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m,n = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(-1,0),(1,0),]

        def dfs(i,j):
            if not(0<=i<m) or not(0<=j<n) or grid[i][j] != 1: return 0
            grid[i][j] = '#'
            return 1 + sum(dfs(i+dr,j+dc) for dr,dc in dirs)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(dfs(i,j), res)

        return res