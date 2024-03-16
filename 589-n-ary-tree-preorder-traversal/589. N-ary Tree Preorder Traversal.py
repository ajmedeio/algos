"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        out = []
        curr = root
        s = []
        s.append(curr)
        while s:
            curr = s.pop()
            out.append(curr.val)
            s.extend(curr.children[::-1])
        
        return out