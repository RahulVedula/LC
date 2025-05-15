class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        e0, e1, e01, e10, e101, e010 = 0,0,0,0,0,0
        for bit in s:
            if bit == '0':
                e0 +=1
                e10 += e1
                e010 += e01
            else:
                e1 +=1
                e01 += e0
                e101 += e10
        return e101 + e010
        
