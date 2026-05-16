class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        i = 0
        ans = ""
        while(i != length1 and i != length2):
            ans += word1[i]
            ans += word2[i]
            i+=1
        if i == length1 and i < length2:
            ans += word2[i:length2]
        if i == length2 and i < length1:
            ans += word1[i:length1]
        
        return ans


