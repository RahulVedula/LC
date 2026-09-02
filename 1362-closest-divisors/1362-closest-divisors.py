class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def getSmallestDivisor(num):
            min_difference = float("inf")
            min_values = []
            for i in range(1, int(sqrt(num))+1):
                if num % i == 0 and abs(num//i - i) < min_difference:
                    min_difference = abs(num//i - i)
                    min_values = [i, num//i]
            return min_values
        
        num1 = getSmallestDivisor(num+1)
        num2 = getSmallestDivisor(num+2)

        return num1 if abs(num1[0] - num1[1]) <= abs(num2[1] - num2[0]) else num2
        