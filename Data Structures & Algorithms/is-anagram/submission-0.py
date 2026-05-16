class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_freq = {}
        s_freq = {}

        # If they are not the same length then automatically return false
        if len(s) != len(t): 
            return False
        
        # Going to try to use a hashmap solution
        for char in s: 
            s_freq[char] =  s_freq.get(char, 0) + 1

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
        
        for key, value in s_freq.items():
            if t_freq.get(key) is None: 
                return False
            if t_freq.get(key) != value: 
                return False
            if t_freq.get(key) == value: 
                continue
        
        return True
