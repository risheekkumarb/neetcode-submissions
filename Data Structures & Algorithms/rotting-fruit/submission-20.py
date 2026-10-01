from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q = deque([])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: q.append((i,j))
                if grid[i][j] == 1: fresh += 1

        time = 0
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        while fresh>0 and q:
            time += 1
            qLen = len(q)
            for _ in range(qLen):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1

        return -1 if fresh else time