class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hMap = {}
        length = len(nums)
        for i in range(0,length):
            if nums[i] in hMap:
                value = hMap[nums[i]]
                if abs(i - value) <= k:
                    return True
                else:
                    hMap[nums[i]] = i
            else:
                hMap[nums[i]] = i
        
        return False