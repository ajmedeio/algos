# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> List[List[int]]:
        out, stack, total = [], [], 0
        def recurse(node: TreeNode):
            nonlocal total
            if node == None:
                return
            
            stack.append(node.val)
            total += node.val
            if node.left == None and node.right == None:
                if total == t:
                    out.append(stack.copy())
            recurse(node.left)
            recurse(node.right)
            total -= node.val
            stack.pop()

        recurse(root)
        return out
