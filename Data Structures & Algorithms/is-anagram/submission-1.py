class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_length = len(t)
        s_length = len(s)
        alphas = [0] * 26
        if s_length != s_length:
            return False
        
        for index, char in enumerate(s):
            alphas[ord(char) - ord('a')] += 1
        
        for index, char in enumerate(t):
            alphas[ord(char) - ord('a')] -=1
        
        for i in alphas:
            if i == 0:
                continue
            else: 
                return False
        return True 