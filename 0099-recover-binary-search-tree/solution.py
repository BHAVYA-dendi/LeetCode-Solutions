class Solution:
    def recoverTree(self, root):
        first = second = prev = None
        cur = root
        stack = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if prev and prev.val > cur.val:
                if first is None:
                    first = prev
                second = cur

            prev = cur
            cur = cur.right

        first.val, second.val = second.val, first.val
