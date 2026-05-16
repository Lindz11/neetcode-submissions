class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            Need to retry this problem using a
        '''
        hSet = set()
        for n in nums:
            if n in hSet: 
                return n
            else: 
                hSet.add(n)