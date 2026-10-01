class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        def dfs(r,c,i):
            if board[r][c] != word[i]: return False
            if i == len(word)-1: return True
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            temp = board[r][c]
            board[r][c] = '#'
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<m and 0<=nc<n:
                    if dfs(nr,nc,i+1):
                        board[r][c] = temp
                        return True
            board[r][c] = temp
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True

        return False