class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sort = sorted(s)
            sorted_string = "".join(sort)
            if sorted_string in anagrams:
                anagrams[sorted_string].append(s)
            else:
                anagrams[sorted_string] = []
                anagrams[sorted_string].append(s)
        
        ans = []

        for value in anagrams.values():
            ans.append(value)
            
        return ans
