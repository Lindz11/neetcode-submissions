class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        place = 0; 
        for i in range(0, length):
            if nums[i] == val: 
                continue
            else: 
                nums[place] = nums[i]
                place += 1
            
        
        return place