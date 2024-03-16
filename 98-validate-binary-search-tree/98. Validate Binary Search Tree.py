# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        s = []
        prev = -math.inf
        curr = root
        while s or curr:
            while curr:
                s.append(curr)
                curr = curr.left
            
            curr = s.pop()
            if curr.val <= prev:
                return False
            
            prev = curr.val
            curr = curr.right
        
        return True
            
            