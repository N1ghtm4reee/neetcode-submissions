# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # for this one we must use BFS with queue and also group nodes at each level
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level = len(q)
            level_nodes = []
            for _ in range(level):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level_nodes.append(node.val)
            res.append(level_nodes)
        return res