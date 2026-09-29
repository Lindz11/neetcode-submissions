class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        length = len(flowerbed)
        # If the number of flowers we need to plant is 0 then we automaitcally have enough space
        if n <= 0:
            return True


        # This solution kind of only works assuming that the length of the array is 2 or more
        for i in range(0, length):
            # If we are at the start of the flower bed and the next cell is empty we can place a flower
            if i == 0 and flowerbed[i] == 0:
                if length > 1 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                if length == 1:
                    flowerbed[i] == 1
                    n-=1
            # If we are just traversing through the flowerbed and somewhere in the middle we can place a 
            # flower then do so 
            elif i + 1 < length - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n-=1
            # If we are at the end of the flowerbed and the cell before was empty then place a flower
            elif i == length - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n-=1
            else: 
                continue
        
        if n <=0:
            return True
        
        return False

