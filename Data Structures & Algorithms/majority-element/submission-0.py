class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        major = len(nums) / 2
        count = 1

        # This solution only works if the array is already sorted
        for i in range(len(nums) - 1): 
            if(nums[i] == nums[i + 1]): 
                count += 1
                if count > major: 
                    return nums[i]
            else: 
                count = 1

        return nums[0]