class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = {}

        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        for key in my_dict.keys():
            if my_dict[key] == 1:
                return key
            
        return -1