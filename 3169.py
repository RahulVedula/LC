class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        sm = sorted(meetings, key=lambda x: x[0])
        arr = []
        start = 1
        end = sm[0][1]
        for i in range(len(sm)):
            if start != sm[i][0]:
                arr.append([start, end])
                start = sm[i][0]
            end = sm[i][1]
        arr.append([start, end])
        start = 0
        res = 0
        print(sm)
        for i in range(len(sm)):
            res += max(0, sm[i][0] - start - 1)
            start =  max(start, sm[i][1])
        res += days - max(start, sm[-1][1])
        return res
        
