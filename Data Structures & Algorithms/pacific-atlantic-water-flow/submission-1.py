class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n  = len(heights), len(heights[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        pc = set()
        ac = set()

        def dfs(i,j,ocean):
            if (i,j) in ocean: return
            ocean.add((i,j))
            for dr,dc in dirs:
                nr,nc = i+dr, j+dc
                if 0<=nr<m and 0<=nc<n and heights[nr][nc] >= heights[i][j]:
                    dfs(nr,nc,ocean)

        for i in range(m):
            dfs(i,0,pc)
            dfs(i,n-1,ac)

        for i in range(n):
            dfs(0,i,pc)
            dfs(m-1,i,ac)

        return list(pc & ac)