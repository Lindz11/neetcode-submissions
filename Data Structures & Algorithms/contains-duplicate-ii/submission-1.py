class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        for i in range(0,length):
            for j in range(i + 1, length):
                if nums[i] == nums[j] and abs(i - j) <=k: 
                    return True
        
        return False