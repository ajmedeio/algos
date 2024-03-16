class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ctr = Counter(words)
        return sorted(ctr.keys(), key = lambda w: (-ctr[w], w))[:k]
    
    
    def topKFrequent1(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        return list({i: j for i, j in sorted(d.items(), key=lambda item:(-item[1], item[0]))}.keys())[:k]
    
    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        wordCounter = Counter(words).most_common()
        out = []
        i = 0
        while i < k:
            currWord = wordCounter.pop(0)
            wordsWithSameFreq = [currWord[0]]
            currFreq = currWord[1]
            while wordCounter and currFreq == wordCounter[0][1]:
                insort(wordsWithSameFreq, wordCounter.pop(0)[0])
            while wordsWithSameFreq and i < k:
                i += 1
                out.append(wordsWithSameFreq.pop(0))
        
        return out
