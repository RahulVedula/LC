class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        upper_bound = max(n, r)
        lower_bound = min(n, r)
        primes = [True] * (upper_bound +1)
        primes[0], primes[1] = False, False
        total_sum = 0

        for i in range(2, upper_bound + 1):
            if not primes[i]:
                continue

            for j in range(i**2, upper_bound+1, i):
                primes[j] = False
        
        for num in range(lower_bound, upper_bound+1):
            if primes[num]:
                total_sum += num
                
        return total_sum
        