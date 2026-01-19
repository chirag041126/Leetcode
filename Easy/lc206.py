class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
s=Solution()
l=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
r=s.reverseList(l)
while r:
    print(r.val)  # Output: 5 4 3 2 1
    r=r.next