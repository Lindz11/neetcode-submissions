class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        length = len(words)
        seen = set()
        for i in range (0, length):
            curr_word = words[i]
            for j in range(0, length):
                if curr_word in words[j] and curr_word != words[j]:
                    seen.add(curr_word)
        ans = list(seen)
        return ans