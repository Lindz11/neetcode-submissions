class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
            The only way I can think of this solution is if the list is already sorted
        '''
        hSet = set()
        length = len(nums)
        print(length)
        for num in nums:
           hSet.add(num)
        
        for i in range(0, length + 1):
            if i not in hSet: 
                return i

        
        return -1