class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        ms = defaultdict(lambda: 0)
        bulls = 0
        cows = 0
        
        for i, cs in enumerate(secret):
            cg = guess[i]
            if cs == cg:
                bulls += 1
            else:
                if ms[cs] < 0:
                    cows += 1
                if ms[cg] > 0:
                    cows += 1
                ms[cg] -= 1
                ms[cs] += 1
            
                
        return str(bulls) + "A" + str(cows) + "B"
