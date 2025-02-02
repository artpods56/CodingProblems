#lc_234:02_02_2024
#https://leetcode.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode):
        current = two_nodes_ahead = head
        reversed_half = None

        while two_nodes_ahead and two_nodes_ahead.next: # check if we made the two node jump and if is there another one in front of us
            two_nodes_ahead = two_nodes_ahead.next.next # jumps two nodes forward

            next_node = current.next  # save pointer for next node

            current.next = reversed_half  # reverse head with tail
            reversed_half = current       
            current = next_node  # move to the next node

        if two_nodes_ahead: # amount of nodes could be odd, if yes then jumping one node forward would place us on the middle one
            current = current.next

        while reversed_half and reversed_half.val == current.val: # loop over both linked lists and compare values
            reversed_half = reversed_half.next
            current = current.next

        return not reversed_half # head should be equal to None if the linked lists were palindroms, that gives us True after negation
        
