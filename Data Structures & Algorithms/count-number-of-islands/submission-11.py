class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m,n = len(grid), len(grid[0])

        def dfs(i,j):
            if not(0<=i<m) or not(0<=j<n) or grid[i][j] != '1': return
            grid[i][j] = '0'
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in dirs:
                nr,nc = i+dr, j+dc
                dfs(nr,nc)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1
        return ans