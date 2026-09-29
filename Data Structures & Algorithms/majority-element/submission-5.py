class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {} 
        length = len(nums)
        major = length / 2
        for i in range(0, length):
            if nums[i] not in elements:
                elements[nums[i]] = 1
                if elements[nums[i]] > major:
                    return nums[i]
            else: 
                elements[nums[i]] += 1
                if elements[nums[i]] > major:
                        return nums[i]
        
        return -1
         