"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
def find_bounds(node):
    tail = node
    sentinel = node
    a = node.next
    while a != sentinel:
        if a.val > a.next.val:
            tail = a
        a = a.next
    return tail.next, tail

class Solution:
    def insert(self, node: 'Optional[Node]', v: int) -> 'Node':
        new_node = Node(v, None)
        if node is None:
            head = new_node
            head.next = head
            return head
        head, tail = find_bounds(node)
        if v <= head.val or tail.val <= v:
            new_node.next = head
            tail.next = new_node
            return node

        a, b = head, head.next
        while True:
            if a.val <= v <= b.val:
                break
            a = a.next
            b = b.next
        a.next = new_node
        new_node.next = b
        return node
