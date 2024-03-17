# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level = 0
        out = []
        levelList = []
        curr = None
        q = [root]
        levelListNodes = []
        while q:
            while q:
                curr = q.pop(0)
                levelList.append(curr.val)
                levelListNodes.append(curr)
            out.append(levelList)
            
            for e in levelListNodes:
                q.append(e.left) if e.left else None
                q.append(e.right) if e.right else None
                
            levelList = []
            levelListNodes = []
            
        return out
            
