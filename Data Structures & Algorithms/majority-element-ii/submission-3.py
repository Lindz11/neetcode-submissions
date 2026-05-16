class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        return_list = []
        benchmark = len(nums)//3
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num,freq in count.items():
            if freq>benchmark:
                return_list.append(num)
        return return_list
        