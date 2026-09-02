class Solution(object):
    def isPalindrome(self, x):
        check = 100
        if x < 0:
            return False
        res = [int(q) for q in str(x)]
        for i in range (0,int(len(res))/2):
            if (res[i] != res[len(res)-1-i]):
                return False 
        
        return True 