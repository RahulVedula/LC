class Solution(object):
    def canJump(self, nums):
        max_reach = nums[0]
        for i in range(1,len(nums)):
            if max_reach < i:
                return False
            max_reach = max(nums[i] + i, max_reach)
        return True
        
