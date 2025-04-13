# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.root = self.fix(root, 0)
    def fix(self, node, val):
        if node:
            node.val = val
            self.arr.append(val)
            self.fix(node.left, (2*val+1))
            self.fix(node.right, (2*val+2))
        return node
    def find(self, target: int) -> bool:
        def helper(node, target):
            if not node:
                return False
            elif node.val == target:
                return True
            return helper(node.left, target) or helper(node.right, target)
        return helper(self.root, target)
        
        
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
