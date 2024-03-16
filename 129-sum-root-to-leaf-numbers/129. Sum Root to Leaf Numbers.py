class Solution:
    def sumNumbers(self, root: TreeNode):
        def preorder(r, curr_number):
            if r is None:
                return
            
            curr_number = curr_number * 10 + r.val
            if r.left is None and r.right is None:
                nonlocal total
                total += curr_number
                
            preorder(r.left, curr_number)
            preorder(r.right, curr_number) 
        
        total = 0
        preorder(root, 0)
        return total