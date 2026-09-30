class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hMap = {}

        for string in arr:
            if string in hMap:
                hMap[string] +=1
            else: 
                hMap[string] = 1
        
        for string in arr: 
            # If the value is distinct meaning 1 and k is 0 then just return we are at the answer we want
            if hMap[string] == 1:
                k -= 1
                if k == 0:
                    return string
        
        return ""