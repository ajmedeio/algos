class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, y - x)
        return -heapq.heappop(stones) if stones else 0
    
    def lastStoneWeightSortedSolution(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if x != y:
                insort(stones, y - x)
        
        return stones.pop() if stones else 0
