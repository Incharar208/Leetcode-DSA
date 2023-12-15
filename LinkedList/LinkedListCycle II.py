class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first we need to find if the linked list has loop
        # only if the linked list has a loop , then the linked list begin point can be identified
        slow = head
        fast = head
        # a loop exists in a linked list when slow and fast pointers meet at a point
        while fast != None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                # move until slow and fast meets again
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow
            # if there is no point where slow and fast meet , then there is no cycle in the linked list
  
        return None
        
       
