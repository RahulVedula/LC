class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_freq = Counter(p)
        s_freq = defaultdict(int)
        left = 0
        for right in range (len(s)):
            s_freq[s[right]] += 1
            if right - left + 1 > len(p):
                s_freq[s[left]] -= 1
                if s_freq[s[left]] == 0: del[s_freq[s[left]]]
                left += 1

            if right - left + 1 == len(p) and s_freq == p_freq:
                result.append(left)

        return result

        