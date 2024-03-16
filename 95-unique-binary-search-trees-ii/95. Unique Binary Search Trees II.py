# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        memo = {}
        def rec(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            if start > end:
                return [None]
            
            out = []
            for i in range(start, end+1):
                # combine all the left with all the right, this is sorta multiplication
                # but we're enumerating them
                for l_tree in rec(start, i-1):
                    for r_tree in rec(i+1, end):
                        # create the current combination of root, left, right and append to out
                        n = TreeNode(i, l_tree, r_tree)
                        out.append(n)
            
            memo[(start, end)] = out
            return out

        return rec(1, n)
