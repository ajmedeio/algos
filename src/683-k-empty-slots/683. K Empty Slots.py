class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        n = len(bulbs)
        b = [0] * n
        for i, x in enumerate(bulbs):
            b[x-1] = 1
            start, end = None, None
            for j in range(n):
                if b[j] == 1 and start is None:
                    start = j
                elif b[j] == 1:
                    end = j
                    run = end - start - 1
                    if run == k:
                        return i + 1
                    else:
                        start = end
                        end = None
        
        return -1
        