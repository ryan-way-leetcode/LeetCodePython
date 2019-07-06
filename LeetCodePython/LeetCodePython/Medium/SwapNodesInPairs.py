# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode):
        #BASE CASES
        if head == None or head.next == None: return head

        #at least two nodes
        first = head
        second = head.next
        head = second
        
        swap = True

        while(first != None and second != None):
            if(swap):
                first.next = second.next
                second.next = first
                second = first.next
                swap = False
            else:
                if(second.next == None): return head
                first.next = second.next
                first = second
                second = second.next
                swap = True

        return head