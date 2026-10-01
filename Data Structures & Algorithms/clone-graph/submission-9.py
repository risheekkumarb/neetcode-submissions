"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        
        def dfs(root):
            if not root: return
            if root in clones: return clones[root]
            new_node = Node(root.val)
            clones[root] = new_node
            for child in root.neighbors:
                new_node.neighbors.append(dfs(child))
            return new_node
        
        return dfs(node)