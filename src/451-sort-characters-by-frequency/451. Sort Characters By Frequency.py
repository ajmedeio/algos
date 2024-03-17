class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([c * freq for c, freq in Counter(s).most_common()])

