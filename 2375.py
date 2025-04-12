class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def backtrack(index, path, res, val, digits): 
            if index-1 == len(pattern):
                res.append("".join(path[:]))
                return 
            if index == 0:
                for i in range(1,10):
                    digits.add(i)
                    backtrack(index+1, path + [str(i)], res, i, digits)
                    digits.remove(i)
            elif pattern[index-1] == 'I':
                for i in range(val+1, 10):
                    if i not in digits:
                        digits.add(i)
                        backtrack(index+1, path + [str(i)], res, i, digits)
                        digits.remove(i)
            elif pattern[index-1] == 'D':
                for i in range(1, val):
                    if i not in digits:
                        digits.add(i)
                        backtrack(index+1, path + [str(i)], res, i, digits)
                        digits.remove(i)
            else:
                return 
        res = []
        digits = set()
        backtrack(0, [], res, 9, digits)
        res.sort()
        return res[0]
            
        
