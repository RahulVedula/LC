class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        removed = 0
        for letter in num:
            if removed == k or not stack:
                stack.append(letter)
                continue
            
            while stack and stack[-1] > letter and removed < k:
                stack.pop()
                removed += 1
            
            stack.append(letter)
        
        while removed < k:
            stack.pop()
            removed += 1

        start = 0
        while start < len(stack) and stack[start] == "0":
            start += 1
        
        trimmed = "".join(stack[start:])
        return trimmed if trimmed else "0"
    