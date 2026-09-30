class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = currSubSum = 0
        length = len(nums)
        for i in range (1, length):
            if nums[i] > nums[i - 1]:
                if currSubSum == 0:
                    currSubSum+= nums[i - 1]
                currSubSum += nums[i]
                maxSum = max(maxSum, currSubSum)
            else: 
                currSubSum = 0

        if maxSum == 0:
            return nums[0]
        return maxSum
        