class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = []
        for p, s, e in trips:
            changes.append((s, +p))
            changes.append((e, -p))
        changes.sort()
        passengers = 0
        for _, p in changes:
            passengers += p
            if passengers > capacity:
                return False
        return True
