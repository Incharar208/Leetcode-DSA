# solution using fast and slow pointers
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        front = None

        for i in range(1,n+1):
            fast = fast.next

        if fast == None:
            return head.next
            
        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head






# solution  using traversing
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        prev = head
        front = head
        if head == None:
            return 
        temp = head
        while temp != None and temp.next != None:
            count = count + 1
            temp = temp.next
        
        value = count - n
        #that is the case where the first node needs to be deleted
        temp = head
        if value == 0:
            head = head.next
            return head

        temp = head
        # suppose n is 1 then the last node needs to be deleted
        if value == count - 1:
            while temp.next != None:
                prev = temp
                temp = temp.next
            prev.next = temp.next
            return head

        # suppose the node to be deleted is any other node somewhere in the middle of the linked list
        else:
            i = 0
            temp = head
            while i != value:
                temp = temp.next
                i = i + 1
            front = temp.next
            temp.next = front.next
            return head
