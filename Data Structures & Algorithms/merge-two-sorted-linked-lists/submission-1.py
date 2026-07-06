# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        head = temp
        count = 0
        while list1 or list2:
            if list1 and list2:
                # print(list1.val , list2.val)
                if list1.val < list2.val:
                    temp1 = ListNode(list1.val)
                    list1 = list1.next
                else:
                    temp1 = ListNode(list2.val)
                    list2 = list2.next
                head.next = temp1
            elif list1:
                # print("Loop 1")
                head.next = list1
                list1 = None
            elif list2:
                # print("Loop 2")
                head.next = list2
                list2 = None
            else:
                break

            # print("val",head.next.val)
            head = head.next
        return temp.next



        