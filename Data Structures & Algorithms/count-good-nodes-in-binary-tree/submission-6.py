# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.ans = 0

        def dfs(node, val):
            if not node: return
            if node.val >= val: self.ans += 1
            dfs(node.left, max(node.val,val))
            dfs(node.right, max(node.val,val))

        dfs(root,float('-inf'))
        return self.ans