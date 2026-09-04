class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(num):
            original_num = num
            new_num = 0
            power = int(round(math.log(num, 10), 4))
            while original_num > 0:
                last_digit = original_num % 10
                original_num = original_num//10
                new_num += last_digit * (10 ** power)
                power -= 1
            
            return new_num

        seen = {}
        min_distance = float("inf")

        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            reverse_num = reverse(num) 
            if reverse_num in seen:
                min_distance = min(min_distance, abs(seen[reverse_num] - i))
            seen[num] = i
    
        return min_distance if min_distance != float("inf") else -1

