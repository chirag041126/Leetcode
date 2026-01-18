class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)      # Left
            result.append(node.val) # Root
            inorder(node.right)     # Right

        inorder(root)
        return result
t=TreeNode(1, None, TreeNode(2, TreeNode(3), None))
s = Solution()
print(s.inorderTraversal(t))  # Output: [1, 3, 2]
print(s.inorderTraversal(None))  # Output: []