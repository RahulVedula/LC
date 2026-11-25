class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        left = 0
        colors = colors + colors[:(k-1)]
        n = len(colors)
        groups = 0
        for right in range(1, n):
            if colors[right] == colors[right - 1]:
                left = right
                continue
            if right - left + 1 >= k: 
                groups += 1
        return groups
