class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        My first thought is just to clone and sort the array and see how many space or not in the same place
        """

        expected = heights.copy()
        expected.sort()
        length = len(heights)
        out_of_place = 0
        for i in range(0, length):
            if expected[i] != heights[i]:
                out_of_place += 1
        
        return out_of_place