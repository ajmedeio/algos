# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(-inf, head)
        i = 0
        a, b = sentinel, head
        while b:
            b = b.next
            if i >= n:
                a = a.next
            i += 1
        if a.next:
            a.next = a.next.next
        return sentinel.next
