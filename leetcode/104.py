# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 104. Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1