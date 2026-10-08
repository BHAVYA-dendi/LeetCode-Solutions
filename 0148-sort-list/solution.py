class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        a = self.sortList(head)
        b = self.sortList(mid)

        dummy = cur = ListNode()
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next

        cur.next = a or b
        return dummy.next
