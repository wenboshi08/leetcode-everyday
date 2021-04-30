# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        ans = [0]
        memo = {0: 1}

        def dfs(root, preSum):
            if not root:
                return
            currSum = preSum + root.val
            if currSum - targetSum in memo:
                ans[0] += memo[currSum - targetSum]
            if currSum in memo:
                memo[currSum] += 1
            else:
                memo[currSum] = 1
            dfs(root.left, currSum)
            dfs(root.right, currSum)
            memo[currSum] -= 1

        dfs(root, 0)
        return ans[0]