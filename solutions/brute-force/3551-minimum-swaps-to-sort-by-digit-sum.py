class Solution:
    def getDigitSum(self, num):
        count = 0
        while num > 0:
            count += num % 10
            num = num//10
        return count

    def minSwaps(self, nums: List[int]) -> int:
        # [1,3,2,0] -> []
        swaps = 0
        sorted_nums = sorted([i for i in range(len(nums))], key=lambda x: (self.getDigitSum(nums[x]), nums[x]))
        number_indices = { sorted_index: i for i, sorted_index in enumerate(sorted_nums)}
        original = [i for i in range(len(nums))]
        position = [i for i in range(len(nums))]

        for i in range(len(nums)):
            if original[i] == sorted_nums[i]:
                continue

            target_index = position[sorted_nums[i]]

            original[i], original[target_index] = original[target_index], original[i]

            position[original[i]] = i
            position[original[target_index]] = target_index

            swaps += 1

        return swaps

            


        
           

