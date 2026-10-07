class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        alphas = [0] * 26
        ans = 0
        # Add all of chars into a set 
        for char in chars:
            alphas[ord(char) - ord('a')] += 1
        
        # Loop through each word and check to see if the current character we are at is in the hSet
        for word in words:
            temp = [0] * 26
            bad = False
            for char in word:
                index = ord(char) - ord('a')
                temp[index] += 1

                if temp[index] > alphas[index]:
                    bad = True
            
            if bad == False:
                ans+= len(word)
            
           

        return ans
            
