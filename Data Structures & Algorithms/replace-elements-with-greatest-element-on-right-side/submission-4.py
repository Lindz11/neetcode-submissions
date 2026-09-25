class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # get length
        length = len(arr)
        # max_num 
        max_num = arr[length - 1]
        arr[length - 1] = -1
        for i in range(length - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_num
            max_num = max(temp, max_num)
        
        arr[length - 1] = -1
        return arr 

