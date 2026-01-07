#Maximum Product of Splitted Binary Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxProduct(self, root):
        all_sum=[]
        def tree_sum(node):
            if node is None:
                return 0
            s=node.val+tree_sum(node.left)+tree_sum(node.right)
            all_sum.append(s)
            return s
        total_sum=tree_sum(root)
        best=0
        for s in all_sum:
            best=max(best,s*(total_sum-s))
        return best%(10**9 + 7)
s= Solution()
# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print(s.maxProduct(root)) #output: 110