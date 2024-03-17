# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode], stoppingNode: Optional[ListNode]) -> bool:
        if head is None:
            return None
        prev = head
        curr = head.next
        while curr and curr is not stoppingNode:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
            
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        tail = self.reverse(middle, None)
        if not tail:
            tail = middle
                
        left = head
        right = tail
        isPalindrome = True
        while left != right and right and right.next != left:
            if left.val != right.val:
                isPalindrome = False
            left = left.next
            right = right.next
        
        afterMiddle = self.reverse(tail, middle)
        middle.next = afterMiddle
        tail.next = None
        
        return isPalindrome
