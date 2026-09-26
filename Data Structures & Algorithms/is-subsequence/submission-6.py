class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Initialize a index to keep track of whats in s and length of s 
        index = 0 
        length = len(s)
        # If we see the same char in both move s forward to the next char
        # Test after if we have hit the length of string s and return True 
        for char in t: 

            if index < length and  char == s[index]:
                index+= 1
        
            if length == index:
                return True

        return False
