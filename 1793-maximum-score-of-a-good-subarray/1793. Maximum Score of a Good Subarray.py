# brute force, consider all possible subarrays (n^2)
# take the score of that subarray which is min of subarray
# times j-i+1
# so it's the smallest subarray times the smallest element between
# i and j that make that subarray
# we can also solve this with a sliding window of sorts
# while potentially looking at a monotonic stack
# we can keep the minimum in the monotonic stack
# so we don't need to compute it on the fly for every
# window we see
# other than that we have a variable sized sliding window
# where the condition of growing is: not yet "good"
# and the condition of shrinking is: we shrink on each iteration
# while we're good, we'll compute stuff and shrink one

class Solution:
    def maximumScore(self, A: List[int], k: int) -> int:
        n = len(A)
        out = 0
        s = [(-1, -1)]
        for i, e in enumerate(A + [0]):
            while s and s[-1][1] >= e:
                minimum = s.pop()[1]
                l = s[-1][0]
                if l < k < i:
                    out = max(out, (i - l - 1) * minimum)
            s.append((i, e))
        return out
