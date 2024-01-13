class Solution:
    def removeDuplicates(self, head):
        if head is None:
            return head

        temp = head
        while temp is not None and temp.next is not None:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
                if temp.next is not None:
                    temp.next.prev = temp
            else:
                temp = temp.next

        return head
