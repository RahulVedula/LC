class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        permutations = []
        counter = Counter(tiles)
        def findAllPermutations(res):
            permutations.append(res)
            for key in counter:
                if counter[key]:
                    counter[key]-=1
                    findAllPermutations(res + [key])    
                    counter[key]+=1
        findAllPermutations([])
        return len(permutations) -1
