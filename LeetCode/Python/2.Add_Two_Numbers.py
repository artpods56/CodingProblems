#lc_2:31_01_2025

 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], overflow = 0) -> Optional[ListNode]:
        node_list = [l1,l2]
        if None in node_list and [isinstance(x,ListNode) for x in node_list].count(True) == 1:
            node_index = node_list.index(None)
            node_list[node_index] = ListNode(0,None)
        val_sum: int = node_list[0].val + node_list[1].val
        l1, l2 = node_list[0], node_list[1]

        if val_sum >= 10:
            for list_node in [l1,l2]:
                if list_node.next == None:
                    list_node.next = ListNode(0,None)
            val_sum = val_sum - 10

            if l1.next != None:
                l1.next.val += 1
            else:
                l1.next = ListNode(1,None)
                l2.next = ListNode(0,None)

        if node_list[0].next or node_list[1].next:
            return ListNode(val_sum, self.addTwoNumbers(node_list[0].next,node_list[1].next))
        else:
            return ListNode(val_sum, None)
