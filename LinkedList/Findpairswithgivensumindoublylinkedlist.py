# GFG QUESTION

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # suppose we have only one node in the linked list, as we need pairs
        if head == None or head.next == None:
            return 
        
        # moving to the last node of the linkedList
        temp = head
        
        while temp.next!= None:
            temp = temp.next
            
        # lets take two pointers 
        # first to traverse from the beginning
        # last to traverse from the end
        # list called answerList to keep the final answer
        answerList = []
        first = head
        last = temp
        
        while first != last and first.data <= last.data:
            if int((first.data + last.data)) == target:
                answerList.append([first.data,last.data])
                first = first.next
                last = last.prev
                
            if int((first.data + last.data)) > target:
                last = last.prev
            
            if int((first.data + last.data)) < target:
                first = first.next
                
        return answerList
