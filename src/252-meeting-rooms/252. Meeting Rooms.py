class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        meetings = sorted(intervals, key=lambda t: t[1])
        prev_meeting_end = -math.inf
        for meeting_start, meeting_end in meetings:
            if prev_meeting_end > meeting_start:
                return False
            prev_meeting_end = meeting_end
        return True
