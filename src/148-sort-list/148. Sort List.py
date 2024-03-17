# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        slowPrev = head
        while fast and fast.next:
            fast = fast.next.next
            slowPrev = slow
            slow = slow.next
            
        return slow, slowPrev
    
    
    def combineList(self, h1: Optional[ListNode], h2: Optional[ListNode]):
        p1 = h1
        p2 = h2
        dummy = ListNode(-1, None)
        out = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                out.next = p1
                p1 = p1.next
            else:
                out.next = p2
                p2 = p2.next
            out = out.next
        out.next = p1 if p1 else p2
        out = dummy.next
        dummy.next = None
        return out
    
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  # 0 or 1 element list, return itself, already sorted
            return head
        # mergesort the linked list
        mid, midLessOne = self.findMid(head)
        midLessOne.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        sortedHead = self.combineList(left, right)
        return sortedHead
        