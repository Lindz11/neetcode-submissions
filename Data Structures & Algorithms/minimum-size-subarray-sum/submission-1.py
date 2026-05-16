class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        min_size = 100000
        cont_sum = 0
        # Loop through the array
        for i in range(0, length): 
            # Keep a continous sum
            cont_sum += nums[i]
            # If we reach a sum greater than or equal to the target
            if cont_sum >= target:
                # Try to decrease the nums in the sum to get the min window 
                while cont_sum - nums[left] >= target:
                    cont_sum -= nums[left]
                    left += 1
                min_size = min(min_size, i - left + 1)
        
        # If we have tried this method and never reach a cont_sum greater than target then return 0
        if cont_sum < target:
            return 0
        
        return min_size