# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,root):
        curr = root
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        temp1, temp2 = head, head
        prev = None
        while temp2 and temp2.next: 
            prev = temp1
            temp1 = temp1.next
            temp2 = temp2.next.next
        if prev:
            prev.next = None
        rev = self.reverse(temp1)

        curr = head
        while curr and rev:
            temp = curr.next
            curr.next = rev
            if not temp:
                break
            rev = rev.next
            curr.next.next = temp
            curr = temp
        

        