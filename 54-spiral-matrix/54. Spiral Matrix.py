class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 1. pop the first row out
        # 2. rotate the matrix 90 counterclockwise
        # 3. repeat 1 until matrix is empty
        
        res = []
        while matrix:
            #1.
            res += matrix.pop(0)
            
            #2.
            matrix[:] = [list(m) for m in zip(*matrix)][::-1]
        return res
    
    def spiralOrder1(self, m: List[List[int]]) -> List[int]:
        minRow = 0
        minCol = 0
        row = 0
        col = 0
        maxRow = len(m) - 1
        maxCol = len(m[0]) - 1
        out = []
        outputLength = len(m) * len(m[0])
        while len(out) < outputLength:
            # move right
            while col <= maxCol:
                out.append(m[row][col])
                col += 1
            if len(out) >= outputLength: break
            minRow += 1
            row += 1
            col -= 1
            # move down
            while row <= maxRow:
                out.append(m[row][col])
                row += 1
            if len(out) >= outputLength: break
            maxCol -= 1
            col -= 1
            row -= 1
            # move left
            while col >= minCol:
                out.append(m[row][col])
                col -= 1
            if len(out) >= outputLength: break
            maxRow -= 1
            row -= 1
            col += 1
            # move up
            while row >= minRow:
                out.append(m[row][col])
                row -= 1
            minCol += 1
            col += 1
            row += 1
            
        return out
