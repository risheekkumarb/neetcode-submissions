from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs from each cell 0
        # at each node set the steps
        # find near by walkable cells and continue

        q = deque([])
        m,n = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: q.append((i,j))
        
        while q:
            i,j = q.popleft()
            for dr,dc in dirs:
                nr,nc = i+dr, j+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 2**31-1:
                    grid[nr][nc] = grid[i][j] + 1
                    q.append((nr,nc))
