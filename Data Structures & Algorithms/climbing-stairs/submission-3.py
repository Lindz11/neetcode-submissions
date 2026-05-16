class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            memo 4 
            memo[3] = memo[3 - 1] + memo [3 - 2]
            memo[3] = memo[2] + memo[1] 
            memo[3] = 2 + 1
            memo[3] = 3 
            memo[4] = memo[4 - 1] + memo[4 - 2]
            memo[4] = memo[3] + memo[2]
            memo[4] = 3 + 2
            memo[4] = 5
        '''
        if n <= 2: 
            return n

        memo = []
        memo = [0] * n
        memo[1] = 2
        memo[0] = 1
        for i in range(2, n):
            # If the last cell is already full then we have a solution just instantly return 
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n - 1]
            