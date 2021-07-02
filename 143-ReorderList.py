# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        pre = None
        cur = slow.next
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        slow.next = None
        
        head1 = head
        head2 = pre
        while head2:
            next = head1.next
            head1.next = head2
            head1 = head2
            head2 = next
