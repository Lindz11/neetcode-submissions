class Solution:
    def maxDifference(self, s: str) -> int:
        alphas = [0] * 26
        max_odd = max_even =  0
        min_even = min_odd = 1000
        for char in s:
            alphas[ord(char) - ord('a')] += 1
        
        for num in alphas:
            if num == 0: 
                continue
            print("The number we are at is", num)
            if num % 2 == 0:
                max_even = max(max_even,num)
                min_even = min(min_even, num)
            else:
                max_odd = max(max_odd,num)
                min_odd = min(min_odd,num)
        
        if  min_odd - max_even >= max_odd - min_even:
            return min_odd - max_even

        return max_odd - min_even

