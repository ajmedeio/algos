# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def rec(i) -> List[Optional[TreeNode]]:
            if i in memo:
                return memo[i]
            
            if i % 2 == 0:
                return []
            if i == 1:
                return [TreeNode(0)]

            out = []
            for k in range(2, i, 2):
                for l in rec(k-1):
                    for r in rec(i-k):
                        node = TreeNode(0, l, r)
                        out.append(node)
            memo[i] = out
            return out
        return rec(n)