# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # taking two new pointers
        temp1 = None
        temp2 = None
        # two strings to take the values
        number1 = ''
        number2 = ''
        # run through the first linkedlist and copy values to one variable
        temp1 = l1
        while temp1:
            number1 =  str(temp1.val) + number1
            temp1 = temp1.next
        # run through the second linkedlist and copy values to one variable
        temp2 = l2
        while temp2:
            number2 = str(temp2.val) + number2
            temp2 = temp2.next
            # adding the values and converting to string
        newNumber = str(int(number1) + int(number2))
        newNumber = newNumber[::-1]
        # create a new linked list with inital value as 0 
        head = ListNode(0)
        temp = head
        # assign values in the newNumber each to each node of the linkedlist by creating new nodes for each value
        for i in newNumber:
            temp.next = ListNode(int(i))
            temp = temp.next
        # returning the linkedlist excluding the first node as it contains 0 as the value
        return head.next
        
