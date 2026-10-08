class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        first = head
        second = prev

        while second:
            n1, n2 = first.next, second.next
            first.next = second
            second.next = n1
            first, second = n1, n2
