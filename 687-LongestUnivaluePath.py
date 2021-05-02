# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        postorder = [(0, root, None)]
        res = 0
        d = {None: 0}

        while postorder:
            seen, node, parent = postorder.pop()
            if node is None:
                continue
            if not seen:
                postorder.append((1, node, parent))
                postorder.append((0, node.right, node.val))
                postorder.append((0, node.left, node.val))
            else:
                if node.val == parent:
                    d[node] = max(d[node.left], d[node.right]) + 1
                else:
                    d[node] = 0
                res = max(res, d[node.left] + d[node.right])
        return res