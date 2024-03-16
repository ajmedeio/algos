def max_rectangle_in_histogram(heights: list[int]) -> int:
    s = [(-1, -1)]
    area = 0
    for i, e in enumerate(chain(heights, [0])):
        while s and s[-1][1] >= e:
            h = s.pop()[1]
            l = s[-1][0]
            area = max(area, (i - l - 1) * h)
        s.append((i, e))
    return area


def build_histograms(matrix: list[[str]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    out = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(m):
        out[0][j] = int(matrix[0][j])
    for i in range(1, n):
        for j in range(m):
            # increment the count or reset to zero
            if matrix[i][j] == "0":
                out[i][j] = 0
            else:
                out[i][j] = out[i-1][j] + 1
    return out


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        histograms = build_histograms(matrix)
        max_rect = 0
        for histogram in histograms:
            max_rect = max(max_rect, max_rectangle_in_histogram(histogram))
        return max_rect
