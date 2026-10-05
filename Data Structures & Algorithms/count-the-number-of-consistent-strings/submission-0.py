class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hSet = set()
        ans = 0
        for char in allowed: 
            hSet.add(char)
        
        for word in words:
            length = len(word)
            count = 0
            for i in range(0, length):
                if word[i] not in hSet:
                    continue;
                else: 
                    count +=1 
            
            if count == length:
                ans +=1
        
        return ans