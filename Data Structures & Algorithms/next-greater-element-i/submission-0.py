class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            temp = nums1[i]
            nums1[i] = -1
            for j in range(len(nums2)):
                if temp == nums2[j]:
                    for k in range (j, len(nums2)):
                        if nums2[k] > nums2[j]:
                            nums1[i] = nums2[k]
                            break
            
        return nums1

