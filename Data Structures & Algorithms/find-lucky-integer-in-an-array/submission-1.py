class Solution:
    def findLucky(self, arr: List[int]) -> int:
        numbers = [0] * 500
        length = len(numbers)
        max_lucky_number = -1
        for num in arr:
            numbers[num] += 1
        
        for i in range(1,length):
            if numbers[i] == i:
                max_lucky_number = max(max_lucky_number,i)
                
                
        
        return max_lucky_number
