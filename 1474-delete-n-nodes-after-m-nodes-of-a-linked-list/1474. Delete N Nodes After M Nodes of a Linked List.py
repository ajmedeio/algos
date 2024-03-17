# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinel = ListNode(-inf, head)
        a, b = sentinel, head
        m_i = 1
        while b and b.next:
            if m_i % m == 0:
                # start skipping nodes
                c = b
                for _ in range(n+1):
                    if c:
                        c = c.next
                b.next = c
            # increment to next position
            a, b = a.next, b.next
            m_i += 1
        return sentinel.next
