class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthElement(nums1, nums2, k):
            if not nums1: return nums2[k]
            if not nums2: return nums1[k]

            m1 = len(nums1)//2
            m2 = len(nums2)//2
            
            if k > m1 + m2:
                if nums1[m1] < nums2[m2]:
                    return findKthElement(nums1[m1+1:], nums2, k-m1-1)
                else:
                    return findKthElement(nums1, nums2[m2+1:], k-m2-1)
            else:
                if nums1[m1] < nums2[m2]:
                    return findKthElement(nums1, nums2[:m2], k)
                else:
                    return findKthElement(nums1[:m1], nums2, k)
        
        length = len(nums1) + len(nums2)
        if length%2 == 0:
            median_lower = findKthElement(nums1, nums2, (length//2)-1)
            median_upper = findKthElement(nums1, nums2, length//2)
            return (median_lower + median_upper)/2
        return findKthElement(nums1, nums2, length//2)