# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        # If one of the nodes we are at is none and the other isn't then we have his a inconsistency in the tree
        if p is None and q is not None or q is None and p is not None: 
            return False
        
        # If the two nodes we are at are not the same then we have hit an inconsistency in the tree 
        elif p.val != q.val:
            return False
        # Otherwise keep traversing the deep left, deep right
        else:
            
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        