class Solution:
    
    def moveToNext(self, digits: set, h, m) -> str:
        # keep counting up from current h and m
        # when min goes to 60, increment h until it reaches 24 where we reset both to 0
        while True:
            m += 1
            if m == 60:
                h += 1
                m = 0
                if h == 24:
                    h = 0
                    m = 0
            if set(f'{h:02d}{m:02d}').issubset(digits):
                return f'{h:02d}:{m:02d}'
            
        
    def nextClosestTime(self, time: str) -> str:
        h, m = time.split(':')
        return self.moveToNext(set(time.replace(':', '')), int(h), int(m))