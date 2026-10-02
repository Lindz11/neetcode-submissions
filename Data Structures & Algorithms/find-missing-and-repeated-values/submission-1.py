class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        length = len(grid)
        hSet = set()
        ans = []
        for row in grid:
            for element in row:
                if element in hSet:
                    ans.append(element)
                hSet.add(element)

        for i in range(1, length*length + 1):
            print(i)
            if i in hSet:
                continue
            else:
                ans.append(i)
        return ans