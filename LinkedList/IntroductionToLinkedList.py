'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Solution:
    def constructLL(self, arr):
        head = Node(arr[0])
        temp = head
        n = len(arr)
        for i in range(1, n):
            temp.next = Node(arr[i])
            temp = temp.next
        return head
