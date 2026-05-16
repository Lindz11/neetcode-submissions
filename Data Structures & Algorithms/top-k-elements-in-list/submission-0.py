class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        sorted_frequency = sorted(freq.items(), key = lambda item: item[1], reverse = True)

        sorted_dict = dict(sorted_frequency)
        ans = []
        print(sorted_dict)
        for key, value in sorted_dict.items():
            if len(ans) == k:
                return ans
            ans.append(key)
        
        return ans
