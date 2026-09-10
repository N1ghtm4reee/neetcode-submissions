# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        s = [root]
        while s:
            node = s.pop()
            if (node.val >= p.val and node.val <= q.val) or (node.val <= p.val and node.val >= q.val):
                ancestor = node
            if node.val > p.val and node.val > q.val and node.left:
                s.append(node.left)
            if node.val < p.val and node.val < q.val and node.right:
                s.append(node.right)
        return ancestor