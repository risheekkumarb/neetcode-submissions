class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n  = len(board), len(board[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(i,j):
            if board[i][j] != 'O': return
            board[i][j] = '#'
            for dr,dc in dirs:
                nr,nc = i+dr, j+dc
                if 0<=nr<m and 0<=nc<n and board[nr][nc]=='O':
                    dfs(nr,nc)

        for i in range(m):
            dfs(i  ,0)
            dfs(i,n-1)

        for i in range(n):
            dfs(0  ,i)
            dfs(m-1,i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '#': board[i][j] = 'O'