from collections import OrderedDict

class Solution:
    def brightestPosition(self, L: List[List[int]]) -> int:
        """Return the left most position with max brightness"""
        n = len(L)
        B = OrderedDict()
        for p, r in L:
            B[p-r] = B[p-r] + 1 if p-r in B else 1
            B[p+r+1] = B[p+r+1] - 1 if p+r+1 in B else -1
        pre_sum = 0
        max_p = 0
        max_b = 0
        for p in sorted(B.keys()):
            pre_sum += B[p]
            if pre_sum > max_b:
                max_b = pre_sum
                max_p = p
        return max_p
