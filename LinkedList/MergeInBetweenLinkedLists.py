# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # to monitor the a and b values
        count1 = 0
        count2 = 0
        # pointer for list1
        temp1 = list1
        #pointer for list2
        temp2 = list2
        # let us make the second list's pointer be pointing to the last node
        # so that its going to be easy to attach to the first linkedlist
        while temp2.next != None:
            temp2 = temp2.next
        
        pointer1 = temp1
        while count1 != a-1:
            count1 = count1 + 1
            pointer1 = pointer1.next

        pointer2 = temp1
        while count2 != b+1:
            count2 = count2 + 1
            pointer2 = pointer2.next

        pointer1.next = list2
        temp2.next = pointer2

        return list1
