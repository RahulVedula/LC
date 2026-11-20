class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        # Heap
        n, m = len(nums1), len(nums2)
        pairs = []
        smallest_sum = []
        for i, num in enumerate(nums1):
            heapq.heappush(smallest_sum, (num + nums2[0], i, 0))

        while len(pairs) < k:
            current_sum, left_index, right_index = smallest_sum[0]
            heapq.heappop(smallest_sum)
            pairs.append([nums1[left_index], nums2[right_index]])

            if right_index + 1 < m:
                heapq.heappush(smallest_sum, (nums1[left_index] + nums2[right_index+1], left_index, right_index+1))
        return pairs