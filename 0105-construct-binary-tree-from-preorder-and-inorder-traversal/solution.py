# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None

        pos = {x: i for i, x in enumerate(inorder)}

        def build(pl, pr, il, ir):
            if pl > pr:
                return None

            root = TreeNode(preorder[pl])
            k = pos[root.val]
            left = k - il

            root.left = build(pl + 1, pl + left, il, k - 1)
            root.right = build(pl + left + 1, pr, k + 1, ir)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
