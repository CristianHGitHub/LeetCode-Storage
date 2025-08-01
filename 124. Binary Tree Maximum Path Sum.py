# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Only consider positive contributions from left and right
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path that passes through this node (left + right + node)
            current_max = node.val + left + right
            self.max_sum = max(self.max_sum, current_max)

            # Return max path sum that continues upward (either left or right)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
