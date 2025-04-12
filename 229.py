class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        thresh = n//3
        temp = Counter(nums)
        for key in temp:
            if temp[key] > thresh:
                res.append(key)
        return res
        
