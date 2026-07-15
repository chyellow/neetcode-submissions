# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)
        

        add = TreeNode(val, None, None)
        dummy = TreeNode(0, root, None)
        while root:
            if val < root.val:
                if root.left:
                    root = root.left
                else:
                    root.left = add
                    break
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = add
                    break
        
        return dummy.left
            