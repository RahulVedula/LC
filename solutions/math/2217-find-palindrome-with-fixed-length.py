class Solution:
    def kthPalindrome(self, queries: list[int], intLength: int) -> list[int]:
        palindromes = []
        def generatePalindrome(query):
            target = intLength//2 - 1 if intLength % 2 == 0 else intLength//2
            if intLength <= 1:
                return query

            number = 10**target
            number += query - 1
            number = str(number)
            if intLength % 2 == 0:
                return number + number[::-1]
            return number + number[:-1][::-1]

        for query in queries:
            target = intLength//2 - 1 if intLength % 2 == 0 else intLength//2
            if query > 9 * (10**target):
                palindromes.append(-1)
            else:
                palindromes.append(int(generatePalindrome(query)))
        return palindromes
            