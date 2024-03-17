# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        p_val = p.val
        q_val = q.val
        curr = root

        while curr:
            curr_val = curr.val

            if p_val > curr_val and q_val > curr_val:
                curr = curr.right
            elif p_val < curr_val and q_val < curr_val:
                curr = curr.left
            else:
                return curr
        