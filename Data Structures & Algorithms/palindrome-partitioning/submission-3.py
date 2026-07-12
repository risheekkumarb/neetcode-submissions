class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res, path = [], []

        def dfs(i):
            if i == n:
                res.append(path[:])
                return

            for j in range(i, n):
                if self.isPali(s[i:j+1]):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
        
        dfs(0)
        return res

    def isPali(self,w):
        l,r = 0,len(w)-1
        while l<=r:
            if w[l] != w[r]: return False
            l += 1
            r -= 1
        return True