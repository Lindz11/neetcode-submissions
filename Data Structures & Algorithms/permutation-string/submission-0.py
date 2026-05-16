class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s2)
        sub_len = len(s1)
        sort = "".join(sorted(s1))
        for i in range (0, length):
            if i + sub_len > length:
                break;
            substring = s2[i: i + sub_len]
            sorted_substring = "".join(sorted(substring))
            if sorted_substring == sort:
                return True
        
        return False
