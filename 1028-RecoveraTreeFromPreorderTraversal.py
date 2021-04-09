# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # stack[i] track the last node seen at ith level
        stack = []
        i = 0
        while i < len(S):
            level = 0
            val = ""
            # get current level
            while i < len(S) and S[i] == "-":
                level += 1
                i += 1
            # get current value
            while i < len(S) and S[i] != "-":
                val = val + S[i]
                i += 1
            # find the right parent for current level
            while len(stack) > level:
                stack.pop()
            node = TreeNode(int(val))
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)

        return stack[0]