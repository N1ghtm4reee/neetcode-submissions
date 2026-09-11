# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        s = [(root, float("-inf"))]
        res = 0
        while s:
            node, maxV = s.pop()
            if node.val >= maxV:
                res += 1
                maxV = max(maxV, node.val)
            if node.left:
                s.append((node.left, maxV))
            if node.right:
                s.append((node.right, maxV))
        return res