class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])

        def dfs(i,j,idx):
            if idx == len(word): return True
            if not(0<=i<m) or not(0<=j<n) or board[i][j] != word[idx]: return False
            temp = board[i][j]
            board[i][j] = '#'
            res = dfs(i+1,j,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i,j-1,idx+1)
            board[i][j] = temp
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i,j,0): return True

        return False