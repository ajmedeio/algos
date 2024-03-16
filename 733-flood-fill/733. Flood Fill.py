class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if len(image) is 0:
            return image
        if len(image[0]) is 0:
            return image
        
        origColor = image[sr][sc]
        if color is origColor:
            return image
        
        q = [(sr, sc)]
        rl = len(image)
        cl = len(image[0])
        while q:
            r, c = q.pop(0)
            image[r][c] = color
            q.append((r - 1, c)) if r - 1 >= 0 and image[r-1][c] is origColor else None
            q.append((r + 1, c)) if r + 1 < rl and image[r+1][c] is origColor else None
            q.append((r, c - 1)) if c - 1 >= 0 and image[r][c - 1] is origColor else None
            q.append((r, c + 1)) if c + 1 < cl and image[r][c + 1] is origColor else None
        
        return image