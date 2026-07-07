# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,l):
        curr = l
        prev = None

        count = 0
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # rl1, rl2 = self.reverse(l1),self.reverse(l2)
        rl1,rl2 = l1,l2
        total = ListNode(0)
        curr = total
        carry = 0

        while rl1 or rl2:
            if rl1 and rl2:
                res = rl1.val + rl2.val + carry
                rl2 = rl2.next 
                rl1 = rl1.next 
            elif rl1:
                res = rl1.val + carry
                rl1 = rl1.next 
            else:
                res = rl2.val + carry
                rl2 = rl2.next 

            v = res % 10
            carry = res // 10
            print(v,carry)

            curr.next = ListNode(v)
            curr = curr.next

        if carry: 
            curr.next = ListNode(carry)

    
        # return self.reverse(total.next)
        return total.next
        