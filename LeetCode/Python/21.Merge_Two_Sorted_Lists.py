# lc_21:06_02_2025
# https://leetcode.com/problems/merge-two-sorted-lists/


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        current = dummy = ListNode()
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next

        if list1 or list2:
            current.next = list1 if list1 else list2

        return dummy.next
