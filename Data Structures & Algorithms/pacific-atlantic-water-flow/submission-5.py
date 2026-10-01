class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])

        def dfs(r,c,visit):
            if (r,c) in visit: return
            visit.add((r,c))
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if nr in range(m) and nc in range(n) and heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,visit)

        pacific_visit = set()
        atlantic_visit = set()
        for i in range(m):
            dfs(i,0,pacific_visit)
            dfs(i,n-1,atlantic_visit)

        for i in range(n):
            dfs(0,i,pacific_visit)
            dfs(m-1,i,atlantic_visit)

        return list(pacific_visit & atlantic_visit)