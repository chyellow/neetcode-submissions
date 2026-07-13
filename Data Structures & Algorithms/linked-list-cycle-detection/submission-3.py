# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        frog = head
        rabbit = head

        while rabbit and rabbit.next:
            frog = frog.next
            rabbit = rabbit.next.next
            if frog == rabbit:
                return True
        
        return False