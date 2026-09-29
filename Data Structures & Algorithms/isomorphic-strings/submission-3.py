class Solution:
    """
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)
        seen_alphas = set()
        if s_length != t_length:
            return False

        iso = {}
        for i in range(0, s_length):
            if s[i] in iso:
                if iso[s[i]] != t[i]:
                    return False
            elif s[i] not in iso and t[i] in seen_alphas: 
                    return False
            else:
                iso[s[i]] = t[i]
                seen_alphas.add(t[i])

        return True