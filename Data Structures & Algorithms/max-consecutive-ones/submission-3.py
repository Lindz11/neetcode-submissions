class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        max_nums = 0
        for element in nums: 
            if element == 0:
                consec = 0
            else: 
                consec +=1
                max_nums = max(consec, max_nums)
        
        return max_nums
