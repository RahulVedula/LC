class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for bracket in s:
            if stack and bracket == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(bracket)
        return len(stack)
            