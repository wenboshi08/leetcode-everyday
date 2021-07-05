# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        
        jump = dummy
        l = head
        r = head
        
        while True:
            count = 0
            
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre = r
                cur = l
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                jump.next = pre
                jump = l
                l = r
            else:
                return dummy.next
