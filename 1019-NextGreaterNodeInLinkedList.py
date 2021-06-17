# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        res = []
        i = 0
        while head:
            while stack and stack[-1][-1] < head.val:
                index, value = stack.pop()
                res[index] = head.val
            stack.append((i, head.val))
            res.append(0)
            head = head.next
            i += 1
        return res
