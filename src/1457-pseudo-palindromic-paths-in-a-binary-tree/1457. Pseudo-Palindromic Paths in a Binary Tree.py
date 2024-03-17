# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def is_pseudo_palindromic(c: Counter) -> bool:
    odd_count = 0
    for k in c:
        if c[k] % 2 != 0:
            odd_count += 1
    if odd_count > 1:
        return False
    else:
        return True

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        c = Counter()
        out = 0
        def dfs(n: TreeNode):
            nonlocal out
            if n is None:
                return
            
            c[n.val] += 1
            if n.left is None and n.right is None:
                if is_pseudo_palindromic(c):
                    out += 1
            dfs(n.left)
            dfs(n.right)
            c[n.val] -= 1
        dfs(root)
        return out
