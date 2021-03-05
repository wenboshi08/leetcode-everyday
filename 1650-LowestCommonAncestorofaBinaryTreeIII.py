"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        level_p = 0
        n = p.parent
        while n:
            level_p += 1
            n = n.parent

        level_q = 0
        n = q.parent
        while n:
            level_q += 1
            n = n.parent

        if level_p < level_q:
            for _ in range(level_q - level_p):
                q = q.parent
        elif level_q < level_p:
            for _ in range(level_p - level_q):
                p = p.parent

        while p != q:
            p = p.parent
            q = q.parent

        return p