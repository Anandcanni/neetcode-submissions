# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        large_diameter = [0]
        def height(root):
            if root is None:
                return 0
            left_h = height(root.left)
            right_h = height(root.right)
            dia =  left_h + right_h
            large_diameter[0] = max(dia,large_diameter[0])
            return 1 + max(left_h ,right_h)
        height(root)
        return large_diameter[0]


        