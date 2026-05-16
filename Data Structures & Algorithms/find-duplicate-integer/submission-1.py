class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            Need to retry this problem using a fast and slow pointer soluion
        '''
        hSet = set()
        for n in nums:
            if n in hSet: 
                return n
            hSet.add(n)