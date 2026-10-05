class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = 0
        length = len(nums)
        # We don't care if we see the same element again such as [4,4]
        # We shoudl track if there is a sudden switch in the array going from [1,2] to then -> [2,1]
        for i in range(0, length - 1):
            if nums [i] < nums[i + 1]:
                increasing +=1
                print("Its increasing in value")
            elif nums[i] > nums[i + 1]:
                decreasing +=1
                print("Its decreasing in value")
            else: 
                continue

        if increasing > 0 and decreasing > 0: 
                return False
        return True