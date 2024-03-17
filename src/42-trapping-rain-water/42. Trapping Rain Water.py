class Solution:
    def trap(self, H: List[int]) -> int:
        n = len(H)
        i, j = 0, n-1
        out = 0
        left_max, right_max = 0, 0
        while i < j:
            if H[i] < H[j]:  # compute contribution from left (i)
                left_max = max(left_max, H[i])
                out += left_max - H[i]
                i += 1
            else:  # compute contribution from right (j)
                right_max = max(right_max, H[j])
                out += right_max - H[j]
                j -= 1
        return out
