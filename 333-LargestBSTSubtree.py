# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:

        max_count = [0]

        def helper(node):
            if not node:
                return 0, True, float('inf'), -float('inf')

            l_count, l_bst, l_min, l_max = helper(node.left)
            r_count, r_bst, r_min, r_max = helper(node.right)

            count = l_count + r_count + 1
            bst = l_bst and r_bst and node.val > l_max and node.val < r_min
            min_v = min(l_min, r_min, node.val)
            max_v = max(l_max, r_max, node.val)
            if bst:
                max_count[0] = max(max_count[0], count)
            return count, bst, min_v, max_v

        helper(root)

        return max_count[0]