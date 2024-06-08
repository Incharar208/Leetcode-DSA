# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = None
        temp2 = None
        number1 = ''
        number2 = ''

        temp1 = l1
        while temp1:
            number1 = number1 + str(temp1.val)
            temp1 = temp1.next

        temp2 = l2
        while temp2:
            number2 = number2 + str(temp2.val)
            temp2 = temp2.next

        newNumber = str(int(number1) + int(number2))

        head = ListNode(0)
        temp = head

        for i in newNumber:
            temp.next = ListNode(int(i))
            temp = temp.next

        return head.next

        
