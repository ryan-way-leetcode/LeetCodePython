import unittest
import timeit
from Medium.SwapNodesInPairs import Solution, ListNode

class Test_SwapNodesInPairs(unittest.TestCase):
    
    #helpers
    def make_list(self, list):
        if len(list) == 0:
            return None
        
        head = ListNode(list[0])
        temp = head
        for i in range(1,len(list)):
            temp.next = ListNode(list[i])
            temp = temp.next
        return head

    def list_equal(self, exp, act):
        while(exp != None and act != None):
            self.assertEqual(exp.val, act.val)
            exp = exp.next
            act = act.next

        self.assertEqual(exp, None)
        self.assertEqual(act, None)

    def test_Example(self):
        head = self.make_list(range(1,5))
        
        exp = ListNode(2)
        exp.next = ListNode(1)
        exp.next.next = ListNode(4)
        exp.next.next.next = ListNode(3)

        sol = Solution()
        act = sol.swapPairs(head)

        self.list_equal(exp, act)
        



if __name__ == '__main__':
    unittest.main()