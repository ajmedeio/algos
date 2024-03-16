class Solution:
    def numTrees(self, n: int) -> int:
        # the number of nodes on the left is decrementing by one and the number of nodes
        # on the right is incrementing by one for each iteration
        # this is just like the Catalan numbers!!

        f = [0] * (n+1)
        f[0] = 1
        
        for i in range(1, n+1):
            for j in range(1, i+1):
                f[i] += f[j-1] * f[i-j]
        
        return f[-1]
