class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #backtrack
        res = []
        def backtrack(s,front_b, back_b, res, stack):
            if front_b == 0 and back_b == 0 and not stack:
                res.append(s)
            if front_b > 0:
                backtrack(s + '(', front_b - 1, back_b, res, stack + ['('])
            if back_b > 0:
                if stack: node = stack.pop()
                else:
                    return 
                backtrack(s + ')', front_b, back_b-1, res, stack)
                stack.append('(')
        backtrack("", n, n, res, [])
        return res
        
        
