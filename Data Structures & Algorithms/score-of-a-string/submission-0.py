class Solution:
    def scoreOfString(self, s: str) -> int:
        length = len(s)
        score = 0
        for i in range (1, length):
            first = ord(s[i])
            second = ord(s[i - 1])
            value = abs(first - second)
            score += value
        return score