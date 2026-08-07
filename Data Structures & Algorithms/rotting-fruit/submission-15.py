from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n  = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        q    = deque([])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: q.append((i,j))
                if grid[i][j] == 1: fresh += 1

        time = 0
        while q and fresh:
            time += 1
            for i in range(len(q)):
                i,j = q.popleft()
                for dr,dc in dirs:
                    nr,nc = i+dr, j+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
        return time if fresh == 0 else -1
