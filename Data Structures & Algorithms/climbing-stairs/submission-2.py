class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            memo 4 
            memo [3] = memo[3 - 1] + memo [3 - 2]
            memo[3] = memo[2] + memo[1] 
            memo[3] = 2 + 1
            memo[3] = 3 
            memo[4] = memo[4 - 1] + memo[4 - 2]
            memo[4] = memo[3] + memo[2]
            memo[4] = 3 + 2
        '''
        if n <= 2: 
            return n

        memo = []
        memo = [0] * n
        memo[1] = 2
        memo[0] = 1
        for i in range(2, n):
            if(memo[n - 1]): 
                return memo[n - 1]
            else: 
                memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n - 1]
            