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
            b_val = b.val
            should_delete = b.val == b.next.val
            while b and b.val == b_val and should_delete:
                a.next = b.next
                b = a.next
            if not should_delete:
                a = a.next
                b = b.next
        return sentinel.next
