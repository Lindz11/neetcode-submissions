class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hSet = set()
        for n in nums:
            if n in hSet: 
                return n
            else: 
                hSet.add(n)

        return -1
        