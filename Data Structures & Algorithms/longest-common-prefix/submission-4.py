class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        common = strs[0]
        for i in range(1, length):
            first = strs[0]
            word = strs[i]
            prefix = ""
            for j in range (0, len(word)):
                if j > len(first) - 1:
                    break;
                if first[j] == word[j]: 
                    prefix += word[j]
                else: 
                    break
            common = min(prefix, common)

        return common
                   
