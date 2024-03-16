"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        c = head
        out = None
        while c:
            c.next = Node(c.val, c.next, c.random)
            c = c.next.next
        c = head
        while c:
            c.next.random = c.random.next if c.random else None
            c = c.next.next
        c = head
        out = head.next
        head_prime = out
        while c:
            c.next = c.next.next
            out.next = out.next.next if out.next else None
            c = c.next
            out = out.next
        return head_prime
