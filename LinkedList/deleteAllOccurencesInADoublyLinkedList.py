# GFG Question
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def deleteAllOccurOfX(self, head, x):
        temp = head
        while temp!=None:
            # stop if value of node becomes equal to x
            if temp.data == x:
                # to check if the node with value x is the first node
                if temp.prev == None:
                    head = temp.next
                # suppose we have only one single node in the entire linked list this takes care of this condition also as it makes head = None
                    if temp.next != None:
                       # not the only node in the linked list
                       temp.next.prev = None
                    temp = head
                    
                # value of node == x present at somewhere in the middle or end
                else:
                    # applicable for the last node value == x
                    temp.prev.next = temp.next
                    if temp.next != None:
                        temp.next.prev = temp.prev
                    temp = temp.next
                        
            # if value of node not eqaul to x then increment and move    
            else:
                temp = temp.next
                
        return head
