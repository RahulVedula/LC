class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        prefix = []
        ans = []
        for word in words:
            for i in range(len(word)+1):
                if word[:i] != "":
                    prefix.append(word[:i])
        pc = Counter(prefix)
        wordSet = set(words)
        def dfs(board, string, index, i, j):
            if not wordSet:
                return 
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] != "visited":
                temp = board[i][j]
                board[i][j] = "visited"
                newstring = string + temp
                if newstring in pc and pc[newstring] > 0 and newstring in wordSet:
                    res.append(newstring)
                    pc[newstring]-=1
                    wordSet.discard(newstring)
                    dfs(board, newstring, index + 1, i + 1, j) 
                    dfs(board, newstring, index + 1, i - 1, j)
                    dfs(board, newstring, index + 1, i, j + 1)
                    dfs(board, newstring, index + 1, i, j - 1)
                    board[i][j] = temp 
                    return 
                if newstring not in pc or pc[newstring] == 0:
                    board[i][j] = temp
                    return 
                else:
                    dfs(board, newstring, index + 1, i + 1, j) 
                    dfs(board, newstring, index + 1, i - 1, j)
                    dfs(board, newstring, index + 1, i, j + 1)
                    dfs(board, newstring, index + 1, i, j - 1)
                board[i][j] = temp
                newstring = newstring[:len(newstring)-1]
            return 
        for i in range(len(board)):
            for j in range(len(board[0])):
                    dfs(board, "", 0, i, j)
        return res

        
        
