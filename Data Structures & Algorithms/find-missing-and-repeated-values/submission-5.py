class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        length = len(grid)
        hSet = set()
        missing = element = 0
        for row in grid:
            for element in row:
                if element in hSet:
                    double = element
                hSet.add(element)

        for i in range(1, length*length + 1):
            if i not in hSet:
                missing = i
        return [double,missing]