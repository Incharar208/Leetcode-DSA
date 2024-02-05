'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def decimalValue(self, head):
        MOD = 10**9 + 7
        number = ''
        temp = head
        while temp:
            number = number + str(temp.data)
            temp = temp.next
            
        answer = int(number,2) % MOD
            
        return answer
