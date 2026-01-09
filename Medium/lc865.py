# Smallest Subtree with all the Deepest Nodes
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        depth = {None:-1}
        def dfs(node,parent=None):
            if node:
                depth[node]=depth[parent]+1
                dfs(node.left,node)
                dfs(node.right,node)
        dfs(root)
        max_depth = max(depth.values())
        def answer(node):
            if not node or depth.get(node)==max_depth:
                return node
            L = answer(node.left)
            R=answer(node.right)
            if L and R:return node
            if L:return L
            if R:return R
            return None
        return answer(root)
s= Solution()
# Example usage:
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
result = s.subtreeWithAllDeepest(root)
while result:
    print(result.val) 
    print(result.left.val)
    print(result.right.val)
    break  # To avoid infinite loop in this example
        