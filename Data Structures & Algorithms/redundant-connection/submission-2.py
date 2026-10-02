class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = list(range(n+1))
        self.Size   = [1] * (n+1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False # already same group, cannot union

        if self.Size[pu] < self.Size[pv]:
            pu,pv = pv,pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        self.comps -= 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]