# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def solve(root, maxV):
            nonlocal res
            if not root:
                return 0
            if root.val >= maxV:
                res += 1
                maxV = root.val
            left = solve(root.left, maxV)
            right = solve(root.right, maxV)

        solve(root, float("-inf"))
        return res