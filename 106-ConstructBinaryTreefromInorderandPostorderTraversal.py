# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        val = postorder.pop()
        root = TreeNode(val)
        for i in range(len(inorder)):
            if inorder[i] == val:
                break
        left = self.buildTree(inorder[:i], postorder[:i])
        right = self.buildTree(inorder[i+1:], postorder[i:])
        root.left = left
        root.right = right
        return root