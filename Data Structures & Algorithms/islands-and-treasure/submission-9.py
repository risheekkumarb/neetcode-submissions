from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid),len(grid[0])
        q = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: q.append(((i,j),0))
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            (r,c),dist = q.popleft()
            grid[r][c] = dist
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = dist+1
                    q.append(((nr,nc),dist+1))