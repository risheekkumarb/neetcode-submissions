# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        def dfs(node, cnt):
            nonlocal ans, k
            if not node: return None
            dfs(node.left, cnt+1)
            k -= 1
            if k == 0:
                ans = node.val
                return
            dfs(node.right, cnt+1)

        dfs(root, 0)
        return ans