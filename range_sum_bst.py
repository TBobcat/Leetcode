# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    ## recursion sum, make the operation as recursion passes 
    ## down the tree
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root == None:
            return 0   
        elif root.val > high:
            # solution is an object so do self.fn()
            return self.rangeSumBST(root.left, low, high)
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        else:
            # had to use line break to make sure operand was not missing
            return root.val + self.rangeSumBST(root.right, low,high)\
                            + self.rangeSumBST(root.left, low, high)
        