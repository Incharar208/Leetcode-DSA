# GFG SOLUTION.

'''
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  '''
class Solution:
    def sortedInsert(self, head, data):
        # creation of new node
        new_node = Node(data)
        
        # if the linked list is empty, make the new node
        if head == None:
            new_node.next = new_node
            return new_node
        
        # if the new nodes data less than the heads data
        temp = head
        if new_node.data < head.data:
            while temp.next != head:
                temp = temp.next
            temp.next = new_node
            new_node.next = head
            return new_node
            
        
        # if the new nodes data is greater than any other nodes data
        # as we have checked for thr first element , we can check from the second element
        temp = head
        while temp.next != head and temp.next.data < data:
            temp = temp.next
            
        new_node.next = temp.next
        temp.next = new_node
        
        return head
        
