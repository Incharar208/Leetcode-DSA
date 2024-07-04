'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compute(head): 
    temp = head
    string = ''
    # first combining to get the string
    while temp:
        string = string + temp.data
        temp = temp.next
    # now checking if the string is palindrom

    i = 0 
    j = len(string) - 1
    while i < j:
        if string[i] == string[j]:
            i = i + 1
            j = j - 1
        else:
            return False
    return True
