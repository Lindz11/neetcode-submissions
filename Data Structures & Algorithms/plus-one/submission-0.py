class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        my_list = []
        length = len(digits)
        addition = True
        for i in reversed(range(length)):
            if digits[i] + 1 > 9:
                digits[i] = 0
                continue;
            else: 
                digits[i] += 1
                break;
        
        if digits[0] == 0:
            digits.insert(0,1)
        
        return digits 

        