class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Frequency array of each where earliest we have one vowel or no vowels
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        letter_parity = defaultdict(dict)
        letter_parity[(0,0,0,0,0)] = -1
        frequency = defaultdict(int)
        max_length = 0
        n, i = len(s), 0

        while i < n:
            letter = s[i]
            frequency[letter] += 1

            parity = []
            for letter in VOWELS:
                parity.append(frequency[letter]%2)
            tuple_parity = tuple(parity)
            
            if tuple_parity not in letter_parity: letter_parity[tuple_parity] = i

            i += 1
            while i < n and s[i] not in VOWELS: i += 1
            if tuple_parity in letter_parity: max_length = max(max_length, i - 1 - letter_parity[tuple_parity])
            
        return max_length