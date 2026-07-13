class DSU:
    def __init__(self,n):
        self.Parent = list(range(n))
        self.Size   = [1] * (n)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m,n = len(grid), len(grid[0])
        dsu = DSU(m * n)

        def index(r,c): return r * n + c
        dirs = [(0,1),(0,-1),(1,0),(-1,0),]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    for dr, dc in dirs:
                        nr, nc = i+dr, j+dc
                        if 0<=nr<m and 0<=nc<n and grid[nr][nc] == '1':
                            if dsu.union(index(i,j), index(nr,nc)):
                                res -= 1
                            
        return res