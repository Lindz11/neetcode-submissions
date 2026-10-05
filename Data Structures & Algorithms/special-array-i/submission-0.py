class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        length = len(nums)
        even = odd = 0
        if length == 1:
            return True

        for i in range(0,length - 1):
            print(i)
            if nums[i] % 2 == 1:
                odd += 1
            if nums[i + 1] % 2 == 1:
                odd += 1
            if nums[i + 1] % 2 == 0:
                even += 1
            if nums[i] % 2 == 0:
                even +=1
            
            if even > 1 or odd > 1:
                return False
            even = 0
            odd = 0
        
        return True
            