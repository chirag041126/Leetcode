class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next


# Create linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

val = 6

# Call function
sol = Solution()
new_head = sol.removeElements(head, val)

# Print result
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next