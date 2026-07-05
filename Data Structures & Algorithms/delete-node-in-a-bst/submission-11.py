# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        if val < root.val:
            root.left = self.deleteNode(root.left, key)
        elif val > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left: return root.right
            if not root.right: return root.left
            else:
                cur = root.right
                while cur.left: cur = cur.left
                cur.left = root.left
                res = root.right
                del root
                return res

        return root