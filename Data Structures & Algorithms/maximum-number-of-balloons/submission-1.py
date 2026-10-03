class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloons = [0] * 5

        for char in text:
            if char == 'b':
                balloons[0]+=1
            if char == 'a':
                balloons[1]+=1
            if char == 'l':
                balloons[2]+=1
            if char == 'o':
                balloons[3]+=1
            if char == 'n':
                balloons[4]+=1

        print(balloons)
        count = 0
        while all(balloons):
            if balloons[3] - 2 < 0 or balloons[2] - 2 < 0:
                break
            elif balloons[0] - 1 < 0 or balloons[1] - 1 < 0 or balloons[4] - 1 < 0:
                break
            else:
                balloons[0]-=1
                balloons[1]-=1
                balloons[2]-=2
                balloons[3]-=2
                balloons[4]-=1
                count+=1
        
        return count
                