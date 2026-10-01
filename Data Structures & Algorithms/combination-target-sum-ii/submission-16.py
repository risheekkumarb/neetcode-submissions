class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(i, path, csum):
            if csum == target:
                ans.append(path[:])
                return
            if i >= len(candidates): return

            for j in range(i,len(candidates)):
                if csum + candidates[j] > target: continue
                if j>i and candidates[j] == candidates[j-1]: continue
                path.append(candidates[j])
                dfs(j+1,path,csum+candidates[j])
                path.pop()

        dfs(0,[],0)
        return ans