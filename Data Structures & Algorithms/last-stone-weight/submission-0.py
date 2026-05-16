class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            top = stones.pop()
            new_stone = top - stones.pop()
            if new_stone > 0:
                stones.append(new_stone)
        if len(stones) == 0:
            return 0
        return stones[0]