class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        length = len(nums)
        even = odd = 0
        if length == 1:
            return True

        for i in range(0,length - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True
            