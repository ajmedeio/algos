# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1e = l1
        l2e = l2
        head = ListNode()
        runner = head
        while l1e is not None or l2e is not None:
            if l1e is None and l2e is not None:
                runner.next = ListNode(l2e.val)
                l2e = l2e.next
            elif l2e is None and l1e is not None:
                runner.next = ListNode(l1e.val)
                l1e = l1e.next
              
            elif l1e.val <= l2e.val:
                runner.next = ListNode(l1e.val)
                l1e = l1e.next
            else:
                runner.next = ListNode(l2e.val)
                l2e = l2e.next
                
            runner = runner.next
            
        return head.next
        