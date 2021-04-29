# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        res = []

        def helper(path, preSum, node):
            if not node:
                return
            curSum = preSum + node.val
            new_path = path + [node.val]
            if not node.left and not node.right:
                if curSum == targetSum:
                    res.append(new_path[:])
                return
            if node.left:
                helper(new_path, curSum, node.left)
            if node.right:
                helper(new_path, curSum, node.right)

        helper([], 0, root)
        return res