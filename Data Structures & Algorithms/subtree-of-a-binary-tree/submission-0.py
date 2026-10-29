# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        def same_tree(node1, node2):
            # Both trees are empty at this point
            if node1 is None and node2 is None:
                return True

            # Only one tree is empty, so they differ
            if node1 is None or node2 is None:
                return False

            # Current values differ
            if node1.val != node2.val:
                return False

            # Both left and right subtrees must match
            return (
                same_tree(node1.left, node2.left)
                and same_tree(node1.right, node2.right)
            )

        # No possible matching subtree
        if root is None:
            return False

        # Check whether subRoot starts at the current root node
        if same_tree(root, subRoot):
            return True

        # Otherwise search in the left and right subtrees
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )