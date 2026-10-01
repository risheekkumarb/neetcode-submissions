class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def is_pali(s):
            l,r = 0,len(s)-1
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        def dfs(i,path):
            if i >= len(s):
                ans.append(path[:])
                return
            for j in range(i,len(s)):
                if is_pali(s[i:j+1]):
                    path.append(s[i:j+1])
                    dfs(j+1,path)
                    path.pop()

        dfs(0,[])
        return ans



