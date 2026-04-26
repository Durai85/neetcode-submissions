# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(root,k,i):
            if not root:
                return

            dfs(root.left,k,i+1)
            res.append(root.val)
            dfs(root.right,k,i+1)
        dfs(root,k,i)
        return res[k-1]
