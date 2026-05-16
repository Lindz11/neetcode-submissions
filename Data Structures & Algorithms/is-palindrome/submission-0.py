class Solution:
    def isPalindrome(self, s: str) -> bool:
      # I need to loop through the string check if the char is alpha or numeric
        new_string = []
        for char in s: 
            if char.isalnum(): 
                char = char.lower() 
                new_string.append(char)

        left = 0
        right = len(new_string) - 1
        # Going to try to do left and right pivots
        while(left < right): 
            if(new_string[left] == new_string[right]):
                left+= 1
                right-=1
                continue
            else:
                return False

        return True