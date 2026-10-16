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

        visited = set()
        ans = []
        min_len = n

        def dfs(i,l):
            if i >= n or i in visited: return l
            visited.add(i)
            max_len = 0
            for child in adj[i]:
                cur_len = dfs(child,l+1)
                max_len = max(cur_len, max_len) if cur_len else max_len
            return max_len

        for i in range(n):
            ilen = dfs(i,0)
            if ilen < min_len:
                min_len = ilen
                ans = [i]
            elif ilen == min_len: ans.append(i)
            visited.clear()
        
        return ans