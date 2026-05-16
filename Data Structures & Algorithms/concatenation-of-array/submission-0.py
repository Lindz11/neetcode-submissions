class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans_list = [0] * (length * 2)
        
        for i in range(0, length):
            ans_list[i] = nums[i]
            ans_list[length + i] = nums[i]
        
        return ans_list