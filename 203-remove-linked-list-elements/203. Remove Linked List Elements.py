# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(-inf, head)
        a, b = sentinel, head
        while b:
            if b.val == val:
                a.next = b.next
                b = a.next
            else:
                a = a.next
                b = b.next
        return sentinel.next
