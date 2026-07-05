class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def dfs(i,csum,path):
            if csum == target:
                res.append(path[:])
                return
            if i >= n or csum > target: return
            
            for j in range(i,n):
                if j>i and candidates[j] == candidates[j-1]: continue
                if csum + candidates[j] > target: continue
                path.append(candidates[j])
                dfs(j+1,csum+candidates[j],path)
                path.pop()

        dfs(0,0,[])
        return res