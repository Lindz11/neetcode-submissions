class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hSet = set()
        length = len(nums)
        for nums in nums:
            hSet.add(nums)
        
        ans = []
        for i in range(0, length):
            if i + 1 not in hSet:
                ans.append(i + 1)
        
        return ans 