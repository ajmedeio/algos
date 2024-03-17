class Solution:
    def findBall(self, g: List[List[int]]) -> List[int]:
        nCol = len(g[0])
        balls = [i for i in range(nCol)]
        numStuck = 0
        nRow = len(g)
        row = 0
        while row < nRow and numStuck < nCol:
            for col, ballState in enumerate(balls):
                if ballState == -1:
                    continue
                    
                slant = g[row][ballState]
                if slant == 1:
                    if ballState + 1 > nCol - 1 or g[row][ballState + 1] == -1:
                        balls[col] = -1
                        numStuck += 1
                    else:
                        balls[col] = ballState + 1 # moves to the right
                elif slant == -1:
                    if ballState - 1 < 0 or g[row][ballState - 1] == 1:
                        balls[col] = -1
                        numStuck += 1
                    else:
                        balls[col] = ballState - 1 # moves to the left
                
            row += 1
        return balls