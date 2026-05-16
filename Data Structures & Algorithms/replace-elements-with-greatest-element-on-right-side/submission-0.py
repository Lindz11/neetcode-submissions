class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
            Manually make the last item in the array -1
            compare each other item to the item right 
            before it to keep a continous max number seen
        '''
        length = len(arr)
        last_seen = arr[length - 1]
        arr[length - 1] = -1

        for i in range(length - 2, -1, -1):
            print(f"Last seen before its changed is {last_seen}")

            max_num = max(arr[i + 1], last_seen)

            print(f"Max num is {max_num}")

            last_seen = arr[i]

            print(f"Last seen is now {last_seen}")

            arr[i] = max_num

        return arr
            