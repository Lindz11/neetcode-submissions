class Solution:
    '''
        Need to come up with a way to choose the character i want to delete
    '''
    def validPalindrome(self, s: str) -> bool:
        delete = False
        deletedchar = ''
        left = 0 
        right = len(s) - 1
        while(left <= right): 
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            elif s[left] == deletedchar:
                left+= 1
                continue
            elif s[right] == deletedchar:
                right -= 1
                continue
            elif s[left] != s[right] and delete == False:
                delete = True
                deletedchar = s[right]
                right -= 1
            elif s[left] != s[right] and delete:
                return False
    
        return True


