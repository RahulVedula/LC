class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ans = []
        def getParentNodes(root, target, path):
            if not root:
                return 
            if root == target:
                ans.append(path + [root])
                return  
            getParentNodes(root.left, target, path + [root])
            getParentNodes(root.right, target, path + [root])
        
        getParentNodes(root, p, [])
        getParentNodes(root, q, [])

        if len(ans) < 2:
            return None
        for i in range(min(len(ans[0]), len(ans[1]))):
            if ans[0][i] != ans[1][i]: 
                return ans[0][i-1]
        
        return ans[0][min(len(ans[0]), len(ans[1])) - 1]
