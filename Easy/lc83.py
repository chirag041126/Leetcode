# Remove Duplicates from Sorted List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        curr=head
        while curr!=None and curr.next!=None:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head
l=ListNode(1)
l.next=ListNode(1)
l.next.next=ListNode(2)
s=Solution()
res=s.deleteDuplicates(l)
while res!=None:
    print(res.val)
    res=res.next


        