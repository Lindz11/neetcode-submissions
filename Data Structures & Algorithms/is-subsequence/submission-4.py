class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Initialize a index to keep track of whats in s and length of s 
        index = 0 
        length = len(s)
        # We want to 
        for char in t: 
            if index == length:
               break
            if char == s[index]:
                index+= 1
        
        if length == index:
            return True

        return False
