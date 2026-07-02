class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        def dfs(node,depth):
            if not node: return None
            if depth == len(res): res.append([])
            res[depth].append(node.val)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        
        dfs(root,0)
        return res
