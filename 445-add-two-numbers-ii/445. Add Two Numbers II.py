# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        head = None
        c = l1
        while c != None:
            s1.append(c.val)
            c = c.next
        c = l2
        while c != None:
            s2.append(c.val)
            c = c.next

        carry = 0
        while s1 and s2:
            t = s1.pop() + s2.pop() + carry
            carry = t // 10
            new_node = ListNode(t % 10, head)
            head = new_node
        while s1:
            t = s1.pop() + carry
            carry = t // 10
            new_node = ListNode(t % 10, head)
            head = new_node
        while s2:
            t = s2.pop() + carry
            carry = t // 10
            new_node = ListNode(t % 10, head)
            head = new_node
        if carry > 0:
            new_node = ListNode(carry, head)
            head = new_node
        return head
