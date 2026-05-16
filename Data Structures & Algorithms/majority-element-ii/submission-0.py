class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        major = len(nums) / 3
        ans = []
        for n in nums:
            if n in freq:
                freq[n] += 1
            else: 
                freq[n] = 1
        
        for key in freq.keys():
            if freq[key] > major: 
                ans.append(key)
            
        return ans
        