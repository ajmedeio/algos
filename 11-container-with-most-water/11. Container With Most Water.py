class Solution:
    def maxArea(self, H: List[int]) -> int:
        lo, hi = 0, len(H)-1
        area = -inf
        while lo < hi:
            curr = min(H[lo], H[hi]) * (hi-lo)
            area = max(area, curr)
            if H[lo] < H[hi]:
                lo += 1
            else:
                hi -= 1
        return area
            