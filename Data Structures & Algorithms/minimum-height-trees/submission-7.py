from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # adj - adding elems to both nodes
        # dfs any node --> goes to the last node, keep track of visited nodes
        # return length of tree
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = []
        min_len = n

        def dfs(i,parent):
            hgt = 0
            for nei in adj[i]:
                if parent == nei: continue
                hgt = max(hgt, 1+dfs(nei,i))
            return hgt

        for i in range(n):
            ilen = dfs(i,-1)
            if ilen < min_len:
                min_len = ilen
                ans = [i]
            elif ilen == min_len: ans.append(i)
        
        return ans