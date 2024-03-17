class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        serial_id = 0
        m_s = {}  # map word to it's serial ID
        words = s.split(" ")
        for word in words:
            if word in m_s:
                continue
            m_s[word] = serial_id
            serial_id += 1
        word_pattern = [m_s[word] for word in words]

        serial_id = 0
        m_p = {}
        for letter in pattern:
            if letter in m_p:
                continue
            m_p[letter] = serial_id
            serial_id += 1
        letter_pattern = [m_p[letter] for letter in pattern]
        return letter_pattern == word_pattern
