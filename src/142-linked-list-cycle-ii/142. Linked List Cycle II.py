# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head
        has_cycle = False
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                has_cycle = True
                break
        if has_cycle == False:
            return None
        p1, mu = head, 0
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        λ = 1
        p1 = p1.next
        while p1 != p2:
            p1 = p1.next
            λ += 1
        return p1
