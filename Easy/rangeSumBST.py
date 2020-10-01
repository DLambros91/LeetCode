# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total = 0 
        
        # Should root be added to sum
        if root.val >= L and root.val <= R:
            total += root.val
        
        # Iterator for the tree
        self.iterator = root
        
        # Should we search the left subtree?
        if root.val > L: 
            total += self.inOrderSearch(root.left, 0, L, R)
            
        # Should we search the right subtree?
        if root.val < R:
            total += self.inOrderSearch(root.right, 0, L, R)
        
        return total
            
    def inOrderSearch(self, root: TreeNode, total: int, L: int, R: int) -> int:
        # Is there a tree?
        if root:
            total = self.inOrderSearch(root.left, total, L, R)
            
            if root.val > R:
                return total
            elif root.val >= L:
                total += root.val
            
            total = self.inOrderSearch(root.right, total, L, R)
            
        return total
                
