# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-inf, head)
        a, b = sentinel, head
        while b and b.next:
            if b.val == b.next.val:
                a.next = b.next
                b = a.next
            else:
                a = a.next
                b = b.next
        return sentinel.next
