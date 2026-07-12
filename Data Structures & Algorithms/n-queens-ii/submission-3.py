class Solution:
    def totalNQueens(self, n: int) -> int:
        res, path = 0, []
        cols, diag, diag1 = set(), set(), set()

        def dfs(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(n):
                if c in cols or r+c in diag or r-c in diag1: continue
                QP = '.'*c + 'Q' + '.'*(n-c+1)
                cols.add(c); diag.add(r+c); diag1.add(r-c)
                path.append(QP)
                dfs(r+1)
                path.pop()
                cols.remove(c); diag.remove(r+c); diag1.remove(r-c)
        
        dfs(0)
        return res