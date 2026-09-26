class Solution:
    def scoreOfString(self, s: str) -> int:
        '''
        neetcode 
         ne - et - co - de 

        '''
        asciis = 'a'
        # Keep track of the length and keep a running ans 
        length = len(s)
        ans = 0
        asciis = 'a'
        for i in range(0, length - 1):
            first = ord(s[i]) - ord(asciis)
            second = ord(s[i + 1]) - ord(asciis)
            ans += abs(second - first)
        
        return ans 
        



        