class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        s = [(-1,-1)]
        for i, height in enumerate(chain(heights, [0])):
            while s and s[-1][1] >= height:
                h = s.pop()[1]
                l = s[-1][0]
                area = max(area, (i - l - 1) * h)
            s.append((i, height))
        return area