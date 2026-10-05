class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        Last attempted: 10/5/2026
        Time: 6 mins, 
        Space Complexity: 0(1) constant varaible space, Time Complexity: 0(N) with N = th elength of nums
        """
        increasing = decreasing = 0
        length = len(nums)
        # We don't care if we see the same element again such as [4,4]
        # We shoudl track if there is a sudden switch in the array going from [1,2] to then -> [2,1]
        for i in range(0, length - 1):
            if increasing > 0 and decreasing > 0: 
                return False
            if nums [i] < nums[i + 1]:
                increasing +=1
            elif nums[i] > nums[i + 1]:
                decreasing +=1
            else: 
                continue

        if increasing > 0 and decreasing > 0: 
                return False
        return True