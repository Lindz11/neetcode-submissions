class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = count = 0
        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1
                max_num = max(max_num, count)
        
        return max_num
