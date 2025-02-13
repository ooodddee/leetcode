# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node before head
        dummy = fast = slow = ListNode(next = head)

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move fast to the end, moving slow at the same time
        while fast and fast.next:
            fast, slow = fast.next, slow.next

        # Remove the target node
        slow.next = slow.next.next
        return dummy.next
        