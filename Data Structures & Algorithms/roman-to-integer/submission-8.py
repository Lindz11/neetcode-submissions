class Solution:
    '''
    "XLIX"
        Add 10 
        Add 50 
        Totoal is 60 but X came before L
        need to subtract 2 * X 
        Ttotal is now 40
        Add 1 
        Add 10
        Total is 51 but I came before X
        need to subtract 2 * I
'''
    def romanToInt(self, s: str) -> int:
        roman_numerals = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = 0
        for i in range(0, len(s)):
            character = s[i]
            total += roman_numerals.get(character)

            if i > 0 and character == 'C' and s[i - 1] == 'X' or character == 'L' and s[i - 1] == 'X':
                total -= 20
            if i > 0 and character == 'V' and s[i - 1] == 'I' or character == 'X' and s[i - 1] == 'I':
                total -= 2
            if i > 0 and character == 'D' and s[i - 1] == 'C' or character == 'M' and s[i - 1] == 'C':
                total -= 200
            print(total)
        return total
