class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wd = set(wordDict)
        res, path = [], []

        def dfs(i):
            if i == len(s):
                res.append(' '.join(path[:]))
                return

            for j in range(i,len(s)):
                if s[i:j+1] not in wd: continue
                path.append(s[i:j+1])
                dfs(j+1)
                path.pop()

        dfs(0)
        return res