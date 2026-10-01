class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1, diag2 = set(), set()

        ans = []

        def dfs(r,path):
            if r==n:
                ans.append(path[:])
                return
            
            for c in range(n):
                temp = '.' * c + 'Q' + '.' * (n-c-1)
                if c in cols or r-c in diag1 or r+c in diag2: continue
                cols.add(c)
                diag1.add(r-c)
                diag2.add(r+c)
                path.append(temp)
                dfs(r+1,path)
                path.pop()
                cols.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)

        dfs(0,[])
        return ans