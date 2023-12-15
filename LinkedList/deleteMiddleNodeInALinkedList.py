# solution using fast and slow pointers
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return 
        if head.next == None:
            return 

        slow = head
        fast = head
        fast = fast.next.next

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head
