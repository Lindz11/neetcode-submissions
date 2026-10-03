class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_length = len(t)
        s_length = len(s)
        place = count = 0
        for i in range(0,s_length):
            if place == t_length:
                break
            if s[i] == t[place]:
                place +=1
        
        return t_length - place
        