#lc_2:31_01_2025

 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        carry: bool = False

        while l1 != None or l2 != None or carry != False:
            l1_digit = l1.val if l1 is not None else 0
            l2_digit = l2.val if l2 is not None else 0
            
            l_sum = l1_digit + l2_digit + carry
            carry = l_sum // 10
            digit = l_sum % 10

            new_node = ListNode(digit)
            tail.next = new_node
            tail = tail.next

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

        return dummy.next

