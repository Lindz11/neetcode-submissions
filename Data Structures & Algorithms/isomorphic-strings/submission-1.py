class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso = {}
        keys_seen = set()
        values_seen = set()
        for i in range(len(s)):
            if t[i] not in values_seen and s[i] not in keys_seen: 
                iso[s[i]] = t[i]
                keys_seen.add(s[i])
                values_seen.add(t[i])
            elif s[i] not in keys_seen and t[i] in values_seen:
                return False
            elif t[i] not in values_seen and s[i] in keys_seen:
                return False
            elif iso[s[i]] != t[i]: 
                return False
            else: 
                continue
        
        return True 

