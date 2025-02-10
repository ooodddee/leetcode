# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle node
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        # Reverse the second part of Linked List
        pre, cur = None, slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre, cur = cur, temp
        
        # merge
        h1, h2 = head, pre
        while h2:
            t1, t2 = h1.next, h2.next
            h1.next = h2
            h2.next = t1
            h1, h2 = t1, t2