# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(-1, None)
        c = head
        t = 0
        while l1 or l2:
            if l1:
                t += l1.val
            if l2:
                t += l2.val
            carry = t // 10
            c.next = ListNode(t % 10, None)
            c = c.next
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            t = carry
        if carry > 0:
            c.next = ListNode(t, None)

        return head.next
        