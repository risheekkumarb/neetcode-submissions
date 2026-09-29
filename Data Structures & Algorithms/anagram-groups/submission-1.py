class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            id = ''.join(sorted(s))
            if id in ans: ans[id].append(s)
            else: ans[id] = [s]
        return list(ans.values())