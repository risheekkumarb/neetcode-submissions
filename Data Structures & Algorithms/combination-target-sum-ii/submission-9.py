class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, n = [], len(candidates)
        path = []

        def dfs(i, csum):
            if csum == target:
                res.append(path[:])
                return

            for j in range(i,n):
                if j>i and candidates[j] == candidates[j-1]: continue
                if csum + candidates[j] > target: return
                path.append(candidates[j])
                dfs(j+1,csum+candidates[j])
                path.pop()

        dfs(0,0)
        return res