# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def helper(node):
            if not node:
                return False, False, None
            left_p, left_q, left_lca = helper(node.left)
            right_p, right_q, right_lca = helper(node.right)
            cur_p = left_p or right_p or node == p
            cur_q = left_q or right_q or node == q
            if left_lca and right_lca or node in {p, q}:
                cur_lca = node
            else:
                cur_lca = left_lca or right_lca
            return cur_p, cur_q, cur_lca

        found_p, found_q, lca = helper(root)
        if found_p and found_q:
            return lca

