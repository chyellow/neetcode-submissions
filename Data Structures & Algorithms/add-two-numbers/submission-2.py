# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_total = 0
        i = 1
        while l1:
            l1_total += l1.val * i
            i *= 10
            l1 = l1.next

        l2_total = 0
        i = 1
        while l2:
            l2_total += l2.val * i
            i *= 10
            l2 = l2.next

        total = l1_total + l2_total
        if total == 0:
            return ListNode(0)
        
        head = ListNode(0, None)
        dummy = ListNode(0, head)

        while total != 0:
            value = total % 10
            add = ListNode(value, None)
            total = total // 10
            head.next = add
            head = head.next
        
        return dummy.next.next



