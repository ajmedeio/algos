class Node:
    def __init__(self, val=-inf, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, i: int) -> int:
        node = self.head
        j = 0
        while node and j != i:
            node = node.next
            j += 1
        return node.val if node and j == i else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        node = Node(val, None)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def addAtIndex(self, i: int, val: int) -> None:
        if i < 0:
            return
        sentinel, node = Node(-inf, self.head), Node(val, None)
        a, b = sentinel, self.head
        j = 0
        while b and j != i:
            a, b, j = a.next, b.next, j + 1
        if j == i:
            a.next = node
            node.next = b
        self.head = sentinel.next
        if self.tail is None:
            self.tail = self.head
        elif self.tail.next:
            self.tail = self.tail.next

    def deleteAtIndex(self, i: int) -> None:
        if i < 0:
            return
        sentinel = Node(-inf, self.head)
        a, b = sentinel, self.head
        j = 0
        while b and j != i:
            a, b, j = a.next, b.next, j + 1
        if b and j == i:
            a.next = a.next.next
        self.head = sentinel.next
        if a.next is None:
            self.tail = a
        