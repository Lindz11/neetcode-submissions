class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        major = len(nums) / 3
        ans = []
        for n in nums:
            freq[n] = 1 + freq.get(n,0)
        
        for key in freq.keys():
            if freq[key] > major: 
                ans.append(key)
            
        return ans
        