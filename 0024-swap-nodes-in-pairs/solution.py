class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        cur = dummy

        while cur.next and cur.next.next:
            a = cur.next
            b = a.next

            a.next = b.next
            b.next = a
            cur.next = b

            cur = a

        return dummy.next
