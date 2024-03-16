class Solution:
    def numOfSubarrays(self, A: List[int]) -> int:
        p, even, odd = 0, 1, 0
        for ai in A:
            p += ai
            if p % 2 == 0:
                even += 1
            else:
                odd += 1
        return (even * odd) % ((10 ** 9) + 7)
