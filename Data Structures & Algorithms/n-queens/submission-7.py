class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, path = [], []
        cols, diag1, diag2 = set(), set(), set()
        # chk_pos --> not in same row, same col, same diag1(r+c) and same diag2(r-c)
        
        def dfs(r,c):
            if r == n:
                res.append(path[:])
                return
            for c in range(n):
                if c in cols or r+c in diag1 or r-c in diag2: continue
                QP = '.' * (c) + 'Q' + '.' * (n-c-1)
                cols.add(c)
                diag1.add(r+c)
                diag2.add(r-c)
                path.append(QP)
                dfs(r+1,0)
                cols.remove(c)
                diag1.remove(r+c)
                diag2.remove(r-c)
                path.pop()

        dfs(0,0)
        return res