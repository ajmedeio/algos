class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetings = sorted(intervals, key=lambda t: t[0])
        h = []
        heapq.heappush(h, meetings[0][1])
        for i in range(1, len(meetings)):
            s, e = meetings[i]
            if s >= h[0]:
                heapq.heappop(h)
                heapq.heappush(h, e)
            else:
                heapq.heappush(h, e)
        return len(h)
