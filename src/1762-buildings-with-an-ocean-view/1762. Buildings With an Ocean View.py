class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        has_view = []
        tallest = 0
        for i in reversed(range(n)):
            h = heights[i]
            if h > tallest:
                has_view.append(i)
            tallest = max(tallest, h)

        return reversed(has_view)