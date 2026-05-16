class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hSet = set()
        count = 0
        for i in range(len(nums)): 
            if nums[i] not in hSet: 
                hSet.add(nums[i])
                nums[count] = nums[i]
                count += 1

        return count
        
        
