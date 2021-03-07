# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:

        def findLCA(node):
            if not node:
                return
            if node.val == p or node.val == q:
                return node
            left = findLCA(node.left)
            right = findLCA(node.right)
            if left and right:
                return node
            return left or right

        def distance(LCA, target):
            distance = 0
            queue = [LCA]
            while queue:
                next = []
                for n in queue:
                    if n.val == target:
                        return distance
                    if n.left:
                        next.append(n.left)
                    if n.right:
                        next.append(n.right)
                distance += 1
                queue = next

        LCA = findLCA(root)
        return distance(LCA, p) + distance(LCA, q)