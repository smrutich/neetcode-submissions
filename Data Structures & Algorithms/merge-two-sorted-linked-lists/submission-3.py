# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        head = temp
        while list1 and list2:
            if list1 and list2:
                # print(list1.val , list2.val)
                if list1.val < list2.val:
                    temp1 = ListNode(list1.val)
                    list1 = list1.next
                else:
                    temp1 = ListNode(list2.val)
                    list2 = list2.next
                head.next = temp1
            # print("val",head.next.val)
            head = head.next
        head.next = list1 or list2
        return temp.next



        